from telegram.ext import (
    ConversationHandler
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dao.GroupDAO import GroupDAO

FINALISE_SPLIT = range(1)

def viewSplit(update, context):
    if (not "currGid" in context.user_data) or context.user_data["currGid"] <= 0:
        update.message.reply_text("Please enter a group first.")
        return ConversationHandler.END
    # first need to get list of expenseDTOs
    expenses = GroupDAO().getOutstandingExpensesInGroup(context.user_data["currGid"])
    # then get list of usernames, put all in dictionary 3 (paid, should pay, balance)
    users = GroupDAO().getUsersInGroup(context.user_data["currGid"])
    paidAmounts = {}
    shouldPayAmounts = {}
    balanceAmounts = {}
    for user in users:
        paidAmounts[user] = 0
        shouldPayAmounts[user] = 0
        balanceAmounts[user] = 0
    
    # for each expense:
    msg = ""
    for expense in expenses:
        if expense.getHasSplit():
            continue
        # add amount paid to dict1[creator]
        paidAmounts[expense.getUsername()] += expense.getCost()
        # add amount / length of splitUsernames to each username so dict2[username]
        splitUsers = expense.getSplitUsernames()
        splitAmount = expense.getCost() / len(splitUsers)
        for user in splitUsers:
            shouldPayAmounts[user] += splitAmount
            msg += str(user) + " has paid " + paidAmounts[user] + " and should actually be paying " + shouldPayAmounts[user] + "\n"
    update.message.reply_text(msg)

    # balance[name] = dict1[name] - dict2[name]
    # positive means they should be getting money back
    for user in users:
        balanceAmounts[user] = paidAmounts[user] - shouldPayAmounts[user]
    # sort based on amount (neg to pos)
    sortedUserArray = [k for k, v in sorted(balanceAmounts.items(), key=lambda item: item[1])]

    lowPointer = 0
    highPointer = len(sortedUserArray) - 1
    msg = ""
    # loop
    while lowPointer != highPointer:
        # we will advance either until they reach each other
        lowUser = sortedUserArray[lowPointer]
        highUser = sortedUserArray[highPointer]
        if round(balanceAmounts[lowUser], 2) == 0:
            lowPointer += 1
            continue
        if round(balanceAmounts[highUser], 2) == 0:
            highPointer -= 1
            continue

        # smaller of the abs amounts
        lowUserPay = balanceAmounts[lowUser] * (-1)
        highUserReceive = balanceAmounts[highUser]
        amountToPay = 0
        if lowUserPay > highUserReceive: # low user pays high user the highUserReceive amount
            amountToPay = highUserReceive
        else: # low user pays off everything
            amountToPay = lowUserPay
        msg += str(lowUser) + " pays " + str(highUser) + " " + str(round(amountToPay, 2)) + "\n"
        balanceAmounts[lowUser] += amountToPay
        balanceAmounts[highUser] -= amountToPay


    if msg == "":
        update.message.reply_text("No new expenses to split.")
        return ConversationHandler.END
        
    update.message.reply_text(msg)
    
    keyboardInner = []
    keyboardInner.append(InlineKeyboardButton("Yes", callback_data="Yes"))
    keyboardInner.append(InlineKeyboardButton("No", callback_data="No"))
    keyboard = [keyboardInner]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("WARNING: Continuing will finalise the split, which is an irreversible action. Do you wish to proceed?", reply_markup=reply_markup)
    
    return FINALISE_SPLIT

def finaliseSplit(update, context):
    answer = update.callback_query.data
    if answer == "No":
        update.callback_query.message.edit_text("Stopped split. You may still view split details above.")
        return ConversationHandler.END
    # if yes, edit to loading, do the split, then edit summary --> for each eid, set hasSplit to true --> 1 update statement
    update.callback_query.message.edit_text("Processing split...")
    msg = GroupDAO().setExpensesToSplit(context.user_data["currGid"])
    update.callback_query.message.edit_text(msg)
    return ConversationHandler.END

def cancelSplit(update, context):
    update.message.reply_text("Stopped split.")
    return ConversationHandler.END

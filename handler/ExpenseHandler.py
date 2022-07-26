from telegram.ext import (
    ConversationHandler
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dto.ExpenseDTO import ExpenseDTO
from dao.ExpenseDAO import ExpenseDAO
from dao.GroupDAO import GroupDAO
from price_parser import Price

GET_COST, GET_CURRENCY, GET_DESC, GET_USERS = range(4)
currencies = ["SGD", "Euro"]
EMPTY_CHECKBOX = "☐"
SELECTED_CHECKBOX = "✔"

def addNewExpense(update, context):
    # first need to check if in the group using context
    if (not "currGid" in context.user_data) or context.user_data["currGid"] <= 0:
        update.message.reply_text("Please enter a group first.")
        return ConversationHandler.END
    # then, prompt for amount
    update.message.reply_text("How much did it cost? Please either enter an integer (e.g. 123) or a number to 2 decimal places (e.g. 123.40)")
    return GET_COST

def getCurrencyKeyboard():
    keyboardInner = []
    for currency in currencies:
        keyboardInner.append(InlineKeyboardButton(currency, callback_data=str(currency)))
    keyboard = [keyboardInner]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def getCost(update, context):
    cost = update.message.text
    cost = Price.fromstring(cost)
    context.user_data["cost"] = cost.amount
    reply_markup = getCurrencyKeyboard()
    update.message.reply_text("What currency was it in?", reply_markup=reply_markup)
    return GET_CURRENCY

def getCurrency(update, context):
    context.user_data["currency"] = update.callback_query.data
    update.callback_query.message.edit_text("Selected currency " + str(context.user_data["currency"]))
    update.callback_query.message.reply_text("Enter a short description of the expense.")
    return GET_DESC

def getUsersKeyboard(gid, splitUsers):
    groupUsers = GroupDAO().getUsersInGroup(gid)
    keyboard = []
    keyboardUsers = []
    for user in groupUsers:
        if user in splitUsers:
            keyboardUsers.append(InlineKeyboardButton(SELECTED_CHECKBOX + " " + user, callback_data=str(user)))
        else:
            keyboardUsers.append(InlineKeyboardButton(EMPTY_CHECKBOX + " " + user, callback_data=str(user)))
    keyboard.append(keyboardUsers)
    keyboard.append([InlineKeyboardButton("All", callback_data="all")])
    keyboard.append([InlineKeyboardButton("Done", callback_data="done")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def getDesc(update, context):
    context.user_data["desc"] = update.message.text
    context.user_data["splitUsers"] = []
    reply_markup = getUsersKeyboard(context.user_data["currGid"], context.user_data["splitUsers"])
    update.message.reply_text("Please select users to split between (if you are part of the split, also select yourself)", reply_markup=reply_markup)
    return GET_USERS

def getUsers(update, context):
    if update.callback_query.data == "all":
        groupUsers = GroupDAO().getUsersInGroup(context.user_data["currGid"])
        for user in groupUsers:
            if user not in context.user_data["splitUsers"]:
                context.user_data["splitUsers"].append(user)
        reply_markup = getUsersKeyboard(context.user_data["currGid"], context.user_data["splitUsers"])
        update.callback_query.message.edit_reply_markup(reply_markup=reply_markup)
        return GET_USERS

    if update.callback_query.data == "done":
        # TODO: handle case when none selected
        update.callback_query.message.edit_text("Loading......")
        msg = addExpense(context.user_data["currGid"], update.callback_query.message.chat_id, context.user_data["cost"], context.user_data["currency"], context.user_data["desc"], context.user_data["splitUsers"])
        update.callback_query.message.edit_text(msg)
        return ConversationHandler.END

    if update.callback_query.data in context.user_data["splitUsers"]:
        context.user_data["splitUsers"].remove(update.callback_query.data)
    else:
        context.user_data["splitUsers"].append(update.callback_query.data)

    reply_markup = getUsersKeyboard(context.user_data["currGid"], context.user_data["splitUsers"])
    update.callback_query.message.edit_reply_markup(reply_markup=reply_markup)
    return GET_USERS

def addExpense(gid, uid, cost, currency, desc, splitUsernames):
    expenseToAdd = ExpenseDTO(None, gid, uid, None, cost, currency, desc, False, None, None, splitUsernames)
    return ExpenseDAO().addExpense(expenseToAdd)

def cancel(update, context):
    update.message.reply_text("Aborting creation of expense.")
    return ConversationHandler.END

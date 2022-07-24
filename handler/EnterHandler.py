from telegram.ext import (
    ConversationHandler
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dao.UserDAO import UserDAO

ENTER_GROUP = range(1)

def getGroupOptions(update, context):
    # get accesses
    groupList = UserDAO().getUserGroups(update.message.chat_id)
    if len(groupList) == 0:
        update.message.reply_text("No groups found! Please create or join a group first.")
        return ConversationHandler.END
    # dynamically create keyboard
    keyboardInner = []
    for groupname in groupList:
        keyboardInner.append(InlineKeyboardButton(groupname, callback_data=str(groupname)))
    keyboard = [keyboardInner]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please select a group below to enter:", reply_markup=reply_markup)
    return ENTER_GROUP # only if there is at least 1 option

def enterGroup(update, context):
    # set context to group
    context.user_data["currGroup"] = update.callback_query.data
    update.callback_query.message.edit_text("You're now in group " + str(update.callback_query.data))
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Aborting entering group.")
    return ConversationHandler.END

def remindKeyboard(update, context):
    update.message.reply_text("Please either press one of the buttons or type 'cancel' to stop entering a group.")
    return getGroupOptions(update, context)

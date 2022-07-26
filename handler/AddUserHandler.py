from telegram.ext import (
    ConversationHandler
)
from dao.GroupDAO import GroupDAO

ADD_USERS_TO_GROUP = range(1)

def enterUsers(update, context):
    # first need to check if in the group using context
    if (not "currGid" in context.user_data) or context.user_data["currGid"] <= 0:
        update.message.reply_text("Please enter a group first.")
        return ConversationHandler.END
    # then, prompt for user
    update.message.reply_text("Type 'cancel' at any point to stop.")
    update.message.reply_text("Please enter a comma-separated list of usernames to be added into your group. Example: username1, username2, username3")
    return ADD_USERS_TO_GROUP

def addUsersToGroup(update, context):
    users = update.message.text
    accessNames = list(map(str.strip, users.split(",")))
    msg = GroupDAO().addUsersToGroup(context.user_data["currGid"], accessNames)
    update.message.reply_text(msg)
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Stopped adding users.")
    return ConversationHandler.END
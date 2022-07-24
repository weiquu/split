from telegram.ext import (
    ConversationHandler
)

GETNAME, ADDUSERS = range(2)

def createGroup(update, context):
    update.message.reply_text("Creating a new group! Type 'cancel' at any point to stop its creation")
    update.message.reply_text("First, please enter a name for your group.")
    return GETNAME

def getName(update, context):
    groupName = update.message.text
    update.message.reply_text("Creating a group called " + groupName)
    context.user_data["groupName"] = groupName
    update.message.reply_text("Next, enter a comma-separated list of usernames to be added into your group. Example: username1, username2, username3")
    update.message.reply_text("You can also choose to add users later. If this is the case, just enter your own username alone")
    return ADDUSERS

def addUsers(update, context):
    users = update.message.text
    # TODO: create the group
    update.message.reply_text(context.user_data["groupName"])
    update.message.reply_text(users)
    update.message.reply_text("Okay! Group created. To enter your group and starting adding transactions, use /enter.")
    return ConversationHandler.END

def cancel(update, context):
    context.user_data["groupName"] = ""
    update.message.reply_text("Stopping group creation!")
    return ConversationHandler.END

from telegram.ext import (
    ConversationHandler
)
from dto.GroupDTO import GroupDTO
from dao.GroupDAO import GroupDAO

GETNAME, ADDUSERS = range(2)

def createGroup(update, context):
    update.message.reply_text("Creating a new group! Type 'cancel' at any point to stop its creation")
    update.message.reply_text("First, please enter a name for your group.")
    return GETNAME

def getName(update, context):
    groupName = update.message.text
    # TODO: check if group name already exists
    update.message.reply_text("Creating a group called " + groupName)
    context.user_data["groupName"] = groupName
    update.message.reply_text("Next, enter a comma-separated list of usernames to be added into your group. Example: username1, username2, username3")
    update.message.reply_text("You can also choose to add users later. If this is the case, just enter your own username alone")
    return ADDUSERS

def addUsers(update, context):
    users = update.message.text
    accessNames = list(map(str.strip, users.split(",")))
    groupToAdd = GroupDTO(None, context.user_data["groupName"], update.message.chat_id, update.message.chat.username, None, accessNames)
    msg = GroupDAO().addGroup(groupToAdd)
    update.message.reply_text(msg)
    return ConversationHandler.END

def cancel(update, context):
    context.user_data["groupName"] = ""
    update.message.reply_text("Stopping group creation!")
    return ConversationHandler.END

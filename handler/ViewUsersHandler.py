from dao.GroupDAO import GroupDAO

def viewUsers(update, context):
    # first need to check if in the group using context
    if (not "currGid" in context.user_data) or context.user_data["currGid"] <= 0:
        update.message.reply_text("Please enter a group first.")
        return
    # then, get users in group
    usernames = GroupDAO().getUsersInGroup(context.user_data["currGid"])
    msg = "List of users in " + str(context.user_data["currGroupname"]) + ":\n"
    for username in usernames:
        msg += "- " + str(username) + "\n"
    update.message.reply_text(msg)

from dto.UserDTO import UserDTO
from dao.UserDAO import UserDAO

def start(update, context):
    chat_id = update.message.chat_id
    # update.message.reply_text(chat_id)
    username = update.message.chat.username
    # update.message.reply_text(username)
    userToAdd = UserDTO(chat_id, username)
    success = UserDAO().addUser(userToAdd)
    if (success):
        msg = "Welcome (: This bot is used to track expenses to be split (or your own personal expenses as well)" + '\n'
        msg += "You can type /help to see a list of commands" + '\n\n'
        msg += 'To create a group, use the /creategroup command, and if the group creator has already added you to a group, you can use the /entergroup command' + '\n'
        msg += 'Within the group, use /expense to create a new expense, then enter the relevant details.' + '\n'
        msg += 'Note: When you select the users to split an expense between, you yourself are not automatically included into the split. '
        msg += 'Hence, if you paid your someone else, just select their name (and not your own). If you want to track your own personal expenses, select only your name.\n\n'
        msg += 'message @weiquu for anyth tqvm'
        update.message.reply_text(msg)
    else:
        update.message.reply_text("We are unable to register you at this time. Please try again later.")
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
        update.message.reply_text("Welcome (: Type /help to see a list of commands")
    else:
        update.message.reply_text("We are unable to register you at this time. Please try again later.")
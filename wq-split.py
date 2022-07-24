from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
from dao.UserDAO import UserDAO
from dto.UserDTO import UserDTO
import os
import psycopg2

def startHandler(update, context):
    users = UserDAO().getUsers()
    for user in users:
        update.message.reply_text("uid = " + str(user.getUid()))
        update.message.reply_text("username = " + str(user.getUsername()))

def infoHandler(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(chat_id)

def main():
    # Get bot's token
    token = ""
    with open("token.txt" , "r") as s:
        for line in s:
            token = line.rstrip()

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handler for commands
    dp.add_handler(CommandHandler("start", startHandler))

    # Handler for messages (non-commands)
    dp.add_handler(MessageHandler(Filters.text, infoHandler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()
from telegram.ext import (
    Updater,
    CommandHandler
)
from dao.UserDAO import UserDAO
from handler.MainHandler import (
    START_HANDLER,
    CREATE_GROUP_HANDLER,
    ENTER_HANDLER,
    EXPENSE_HANDLER,
    ADD_USERS_HANDLER,
    VIEW_USERS_HANDLER,
    VIEW_EXPENSES_HANDLER,
    SPLIT_HANDLER
)

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

    # Handlers
    dp.add_handler(START_HANDLER)
    dp.add_handler(CREATE_GROUP_HANDLER)
    dp.add_handler(ENTER_HANDLER)
    dp.add_handler(EXPENSE_HANDLER)
    dp.add_handler(ADD_USERS_HANDLER)
    dp.add_handler(VIEW_USERS_HANDLER)
    dp.add_handler(VIEW_EXPENSES_HANDLER)
    dp.add_handler(SPLIT_HANDLER)

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
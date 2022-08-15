from telegram.ext import (
    Updater,
    CommandHandler
)
from dao.UserDAO import UserDAO
from handler.MainHandler import (
    START_HANDLER,
    CREATE_GROUP_HANDLER,
    ENTER_GROUP_HANDLER,
    EXPENSE_HANDLER,
    ADD_USERS_HANDLER,
    VIEW_OUTSTANDING_HANDLER,
    VIEW_USERS_HANDLER,
    VIEW_EXPENSES_HANDLER,
    SPLIT_HANDLER,
    HELP_HANDLER
)
import os

def main():
    # Get bot's token
    token = os.environ["WQ_SPLIT_TOKEN"]

    # Get bot's port
    port = int(os.environ.get('PORT', 5000))

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(START_HANDLER)
    dp.add_handler(CREATE_GROUP_HANDLER)
    dp.add_handler(ENTER_GROUP_HANDLER)
    dp.add_handler(EXPENSE_HANDLER)
    dp.add_handler(ADD_USERS_HANDLER)
    dp.add_handler(VIEW_USERS_HANDLER)
    dp.add_handler(VIEW_EXPENSES_HANDLER)
    dp.add_handler(VIEW_OUTSTANDING_HANDLER)
    dp.add_handler(SPLIT_HANDLER)
    dp.add_handler(HELP_HANDLER)

    # Start the Bot
    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0", port=int(port), url_path=token)
    updater.bot.setWebhook('https://wq-split.herokuapp.com/' + token)

    updater.idle()

if __name__ == "__main__":
    main()
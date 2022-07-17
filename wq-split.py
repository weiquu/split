from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
import os
import psycopg2

def startHandler(update, context):
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from users"
        cursor.execute(postgreSQL_select_Query)
        user_records = cursor.fetchall()
        for user in user_records:
            update.message.reply_text("uid = " + str(user[0]))
            update.message.reply_text("name = " + str(user[1]))
    except(Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

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
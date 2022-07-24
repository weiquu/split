from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)

ONE, TWO = range(2)

def start(update, context):
    update.message.reply_text("in start method")
    return ONE

def firstState(update, context):
    msg = update.message.text
    update.message.reply_text("in first state method")
    update.message.reply_text(msg)
    return TWO

def secondState(update, context):
    msg = update.message.text
    update.message.reply_text("in second state method")
    update.message.reply_text(msg)
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("in cancel method")
    return ConversationHandler.END
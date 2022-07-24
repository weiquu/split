from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)
from handler.StartHandler import (
    ONE,
    TWO,
    start,
    firstState,
    secondState,
    cancel
)

START_HANDLER = ConversationHandler(entry_points = [CommandHandler('start', start)],
        states = {
            ONE : [MessageHandler(Filters.text & (~Filters.regex('cancel')), firstState)],
            TWO : [MessageHandler(Filters.text & (~Filters.regex('cancel')), secondState)]
        },
        fallbacks = [MessageHandler(Filters.regex('cancel'), cancel)],
        allow_reentry = True
)
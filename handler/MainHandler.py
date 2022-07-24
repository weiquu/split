from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)
from handler.StartHandler import start
from handler.CreateGroupHandler import (
    GETNAME,
    ADDUSERS,
    createGroup,
    getName,
    addUsers,
    cancel
)

START_HANDLER = CommandHandler('start', start)

CREATE_GROUP_HANDLER = ConversationHandler(entry_points = [CommandHandler('creategroup', createGroup)],
        states = {
            GETNAME : [MessageHandler(Filters.text & (~Filters.regex('cancel')), getName)],
            ADDUSERS : [MessageHandler(Filters.text & (~Filters.regex('cancel')), addUsers)]
        },
        fallbacks = [MessageHandler(Filters.regex('cancel'), cancel)],
        allow_reentry = True
)
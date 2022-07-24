from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler,
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
from handler.EnterHandler import (
    ENTER_GROUP,
    getGroupOptions,
    enterGroup,
    cancel,
    remindKeyboard
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

ENTER_HANDLER = ConversationHandler(entry_points = [CommandHandler('enter', getGroupOptions)],
        states = {
            ENTER_GROUP : [CallbackQueryHandler(enterGroup)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancel),
            MessageHandler(Filters.all, remindKeyboard),
        ],
        allow_reentry = True
)
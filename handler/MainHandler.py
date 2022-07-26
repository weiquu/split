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
from handler.ExpenseHandler import (
    GET_COST,
    GET_CURRENCY,
    GET_USERS,
    addNewExpense,
    getCost,
    getCurrency,
    getUsers,
    cancel
)
from handler.AddUserHandler import (
    ADD_USERS_TO_GROUP,
    enterUsers,
    addUsersToGroup,
    cancel
)
from handler.ViewUsersHandler import (
    viewUsers
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
            MessageHandler(Filters.all, remindKeyboard)
        ],
        allow_reentry = True
)

EXPENSE_HANDLER = ConversationHandler(entry_points = [CommandHandler('expense', addNewExpense)],
        states = {
            GET_COST : [MessageHandler(Filters.text & (~Filters.regex('cancel')), getCost)],
            GET_CURRENCY : [CallbackQueryHandler(getCurrency)],
            GET_USERS : [CallbackQueryHandler(getUsers)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancel)
        ],
        allow_reentry = True
)

ADD_USERS_HANDLER = ConversationHandler(entry_points = [CommandHandler('addusers', enterUsers)],
        states = {
            ADD_USERS_TO_GROUP : [MessageHandler(Filters.text & (~Filters.regex('cancel')), addUsersToGroup)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancel)
        ],
        allow_reentry = True
)

VIEW_USERS_HANDLER = CommandHandler('viewusers', viewUsers)

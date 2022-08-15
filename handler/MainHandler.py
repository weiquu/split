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
    cancelCreateGroup
)
from handler.EnterGroupHandler import (
    ENTER_GROUP,
    getGroupOptions,
    enterGroup,
    cancelEnter,
    remindKeyboard
)
from handler.ExpenseHandler import (
    GET_COST,
    GET_CURRENCY,
    GET_DESC,
    GET_USERS,
    addNewExpense,
    getCost,
    getCurrency,
    getDesc,
    getUsers,
    cancelExpense
)
from handler.AddUserHandler import (
    ADD_USERS_TO_GROUP,
    enterUsers,
    addUsersToGroup,
    cancelAddUser
)
from handler.ViewUsersHandler import viewUsers
from handler.ViewExpensesHandler import viewAllExpenses
from handler.ViewOutstandingHandler import viewOutstandingExpenses
from handler.SplitHandler import (
    FINALISE_SPLIT,
    viewSplit,
    finaliseSplit,
    cancelSplit
)
from handler.HelpHandler import help


START_HANDLER = CommandHandler('start', start)

CREATE_GROUP_HANDLER = ConversationHandler(entry_points = [CommandHandler('creategroup', createGroup)],
        states = {
            GETNAME : [MessageHandler(Filters.text & (~Filters.regex('cancel')), getName)],
            ADDUSERS : [MessageHandler(Filters.text & (~Filters.regex('cancel')), addUsers)]
        },
        fallbacks = [MessageHandler(Filters.regex('cancel'), cancelCreateGroup)],
        allow_reentry = True
)

ENTER_GROUP_HANDLER = ConversationHandler(entry_points = [CommandHandler('entergroup', getGroupOptions)],
        states = {
            ENTER_GROUP : [CallbackQueryHandler(enterGroup)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancelEnter),
            MessageHandler(Filters.all, remindKeyboard)
        ],
        allow_reentry = True
)

EXPENSE_HANDLER = ConversationHandler(entry_points = [CommandHandler('expense', addNewExpense)],
        states = {
            GET_COST : [MessageHandler(Filters.text & (~Filters.regex('cancel')), getCost)],
            GET_CURRENCY : [CallbackQueryHandler(getCurrency)],
            GET_DESC : [MessageHandler(Filters.text & (~Filters.regex('cancel')), getDesc)],
            GET_USERS : [CallbackQueryHandler(getUsers)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancelExpense)
        ],
        allow_reentry = True
)

ADD_USERS_HANDLER = ConversationHandler(entry_points = [CommandHandler('addusers', enterUsers)],
        states = {
            ADD_USERS_TO_GROUP : [MessageHandler(Filters.text & (~Filters.regex('cancel')), addUsersToGroup)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancelAddUser)
        ],
        allow_reentry = True
)

VIEW_USERS_HANDLER = CommandHandler('viewusers', viewUsers)

VIEW_EXPENSES_HANDLER = CommandHandler('viewall', viewAllExpenses)

VIEW_OUTSTANDING_HANDLER = CommandHandler('outstanding', viewOutstandingExpenses)

SPLIT_HANDLER = ConversationHandler(entry_points = [CommandHandler('split', viewSplit)],
        states = {
            FINALISE_SPLIT : [CallbackQueryHandler(finaliseSplit)]
        },
        fallbacks = [
            MessageHandler(Filters.regex('cancel'), cancelSplit)
        ],
        allow_reentry = True
)

HELP_HANDLER = CommandHandler('help', help)

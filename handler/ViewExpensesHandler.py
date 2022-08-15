from dao.GroupDAO import GroupDAO
import util.Utilities

def viewAllExpenses(update, context):
    # first need to check if in the group using context
    if (not "currGid" in context.user_data) or context.user_data["currGid"] <= 0:
        update.message.reply_text("Please enter a group first.")
        return
    # then, get expenses in group
    expenses = GroupDAO().getAllExpensesInGroup(context.user_data["currGid"])
    msg = "List of all expenses in " + str(context.user_data["currGroupname"]) + ":\n\n"
    i = 1
    for expense in expenses:
        update.message.reply_text(i)
        splitStatus = ""
        if expense.getHasSplit():
            splitStatus = "has been split."
        else:
            splitStatus = "has not been split."
        msg += str(i) + ": " + str(expense.getCost()) + " (" + str(expense.getCurrency()) + ") for " + str(expense.getExpDesc()) + "\n"
        # TODO: format usernames (done)
        msg += "Paid by " + str(expense.getUsername()) + " and split between " + str(util.Utilities.formatUsernamesFromArray(expense.getSplitUsernames())) + " \n"
        # TODO: format datetime
        msg += "Created at " + str(expense.getDateCreated()) + " and " + splitStatus + "\n\n"
        i += 1
    update.message.reply_text(msg)
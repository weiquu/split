from db.DBAccessor import DBAccessor
from dao.UserDAO import UserDAO
import util.Utilities

class ExpenseDAO:
    __db = None

    def __init__(self):
        self.__db = DBAccessor()

    def addExpense(self, expenseToAdd):
        msg = ""
        eid = self.__db.insertWithReturn("INSERT INTO Expenses (gid, uid, cost, currency, expDesc) VALUES (%s, %s, %s, %s, %s) RETURNING eid",
                (expenseToAdd.getGid(), expenseToAdd.getUid(), expenseToAdd.getCost(), expenseToAdd.getCurrency(), expenseToAdd.getExpDesc()))
        if not eid:
            return "Expense cannot be created at this time. Please try again later."
        msg += "Okay! Expense created.\n"

        # put into splits
        success = True
        for username in expenseToAdd.getSplitUsernames():
            # get the uid
            uid = UserDAO().getUserFromUsername(username)
            # insert into splits values (eid, uid)
            successIndiv = self.__db.insert("INSERT INTO Splits values (%s, %s)", (eid, uid))
            if not successIndiv:
                success = False
                break

        if success:
            msg += "Split between " + util.Utilities.formatUsernamesFromArray(expenseToAdd.getSplitUsernames())
        else:
            msg += "Unable to create split at this time."

        return msg

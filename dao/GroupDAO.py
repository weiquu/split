from db.DBAccessor import DBAccessor
from dto.GroupDTO import GroupDTO

class GroupDAO:
    __db = None

    def __init__(self):
        self.__db = DBAccessor()

    def addGroup(self, groupToAdd):
        msg = ""
        # we only want to insert groupName and creator UID, which we both have, into the groups table
        gid = self.__db.insertWithReturn("INSERT INTO Groups (groupname, creator) VALUES (%s, %s) RETURNING gid",
                (groupToAdd.getGroupname(), groupToAdd.getCreatorUid()))
        if not gid:
            return "Group cannot be created at this time. Please try again later."
        msg += "Okay! Group created. To enter your group and starting adding transactions, use /enter.\n"

        # add owner to access, then below if username = owner just continue
        success = self.__db.insert("INSERT INTO Access values (%s, %s)", (groupToAdd.getCreatorUid(), gid))
        if not success:
            msg += "We are unable to add " + str(groupToAdd.getCreatorName()) + " to the group. Please try again later.\n"

        # for each item in accessNames, we want to get their userid and then add them to the access table
        for username in groupToAdd.getAccessNames():
            if username == groupToAdd.getCreatorName():
                continue
            uidRow = self.__db.select("SELECT uid FROM Users WHERE username = %s", (username,))
            if uidRow.rowcount == 0:
                msg += str(username) + " has yet to be registered. Please direct them to this bot and press /start\n"
                self.__db.insert("INSERT INTO Unregistered values (%s)", (username,))
                continue
            uid = uidRow.fetchone()[0]
            success = self.__db.insert("INSERT INTO Access values (%s, %s)", (uid, gid))
            if not success:
                msg += "We are unable to add " + str(username) + " to the group. Please try again later.\n"
            else:
                msg += "Added " + str(username) + " to the group!\n"
        
        return msg

    def getGidFromGroupname(self, groupname):
        gid = self.__db.select("SELECT gid FROM Groups WHERE groupname = %s", (groupname,))
        if gid.rowcount == 0:
            return -1
        return gid.fetchone()[0]

    def getUsersInGroup(self, gid):
        result = self.__db.select("SELECT U.username FROM Access A NATURAL JOIN Users U WHERE A.gid = %s", (gid,)).fetchall()
        groupUsers = [user[0] for user in result]
        return groupUsers

    def addUsersToGroup(self, gid, usersList):
        msg = ""
        for username in usersList:
            uidRow = self.__db.select("SELECT uid FROM Users WHERE username = %s", (username,))
            if uidRow.rowcount == 0:
                msg += str(username) + " has yet to be registered. Please direct them to this bot and press /start\n"
                self.__db.insert("INSERT INTO Unregistered values (%s)", (username,))
                continue
            uid = uidRow.fetchone()[0]
            accessRow = self.__db.select("SELECT 1 FROM Access WHERE uid = %s AND gid = %s", (uid, gid))
            if accessRow.rowcount == 1: # user alr inside
                msg += str(username) + " is already in the group\n"
                continue
            success = self.__db.insert("INSERT INTO Access values (%s, %s)", (uid, gid))
            if not success:
                msg += "We are unable to add " + str(username) + " to the group. Please try again later.\n"
            else:
                msg += "Added " + str(username) + " to the group!\n"

        return msg

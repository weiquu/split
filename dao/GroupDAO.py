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

        # for each item in accessNames, we want to get their userid and then add them to the access table
        for username in groupToAdd.getAccessNames():
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
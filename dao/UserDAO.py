from db.DBAccessor import DBAccessor
from dto.UserDTO import UserDTO

class UserDAO:
    __db = None

    def __init__(self):
        self.__db = DBAccessor()

    def getAllUsers(self):
        userRecordsDB = self.__db.select("SELECT * FROM users", ()).fetchall()
        users = []
        for user in userRecordsDB:
            userDTO = UserDTO(uid=user[0], username=user[1])
            users.append(userDTO)
        return users

    def isUserRegistered(self, uid):
        result = self.__db.select("SELECT COUNT(*) FROM users WHERE uid = %s", (uid,)).fetchone()
        return (result[0] == 1)

    def getUserFromUsername(self, username):
        result = self.__db.select("SELECT uid FROM users WHERE username = %s", (username,)).fetchone()
        return result[0]

    def addUser(self, userToAdd):
        if (self.isUserRegistered(userToAdd.getUid())): # already registered, we are done
            return True
        return self.__db.insert("INSERT INTO users (uid, username) VALUES (%s, %s)", 
                (userToAdd.getUid(), userToAdd.getUsername()))

    def getUserGroups(self, uid):
        # returns a list of groups that the user has access to
        result = self.__db.select("SELECT G.groupname FROM Access A NATURAL JOIN Groups G WHERE A.uid = %s", (uid,))
        if result.rowcount == 0:
            return []
        result = result.fetchall()
        groupList = [group[0] for group in result]
        return groupList

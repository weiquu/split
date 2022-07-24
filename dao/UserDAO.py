from db.DBAccessor import DBAccessor
from dto.UserDTO import UserDTO

class UserDAO:
    __db = None

    def __init__(self):
        self.__db = DBAccessor()

    def getUsers(self):
        userRecordsDB = self.__db.query("SELECT * FROM users WHERE uid > %s;", (1,)).fetchall()
        users = []
        for user in userRecordsDB:
            userDTO = UserDTO(uid=user[0], username=user[1])
            users.append(userDTO)
        return users
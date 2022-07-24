from dataclasses import dataclass

@dataclass
class UserDTO:
    uid: int
    username: str

    def getUid(self):
        return self.uid

    def getUsername(self):
        return self.username
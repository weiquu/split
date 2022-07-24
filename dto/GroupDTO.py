from dataclasses import dataclass
from typing import List

@dataclass
class GroupDTO:
    gid: int
    groupname: str
    creatorUid: int
    creatorName: str
    accessUids: List[int]
    accessNames: List[str]

    def getGid(self):
        return self.gid

    def getGroupname(self):
        return self.groupname

    def getCreatorUid(self):
        return self.creatorUid

    def getCreatorName(self):
        return self.creatorName

    def getAccessUids(self):
        return self.accessUids

    def getAccessNames(self):
        return self.accessNames
    
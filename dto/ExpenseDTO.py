from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

@dataclass
class ExpenseDTO:
    eid: int
    gid: int
    uid: int
    username: str
    cost: Decimal
    currency: str
    expDesc: str
    hasSplit: bool
    dateCreated: datetime
    splitUids: List[int]
    splitUsernames: List[str]

    def getEid(self):
        return self.eid

    def getGid(self):
        return self.gid

    def getUid(self):
        return self.uid

    def getUsername(self):
        return self.username

    def getCost(self):
        return self.cost

    def getCurrency(self):
        return self.currency

    def getExpDesc(self):
        return self.expDesc

    def getHasSplit(self):
        return self.hasSplit

    def getDateCreated(self):
        return self.dateCreated

    def getSplitUid(self):
        return self.splitUids

    def getSplitUsernames(self):
        return self.splitUsernames
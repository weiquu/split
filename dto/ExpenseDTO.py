from dataclasses import dataclass
from decimal import Decimal
from typing import List

@dataclass
class ExpenseDTO:
    eid: int
    gid: int
    uid: int
    cost: Decimal
    currency: str
    splitUids: List[int]
    splitUsernames: List[str]

    def getEid(self):
        return self.eid

    def getGid(self):
        return self.gid

    def getUid(self):
        return self.uid

    def getCost(self):
        return self.cost

    def getCurrency(self):
        return self.currency

    def getSplitUid(self):
        return self.splitUids

    def getSplitUsernames(self):
        return self.splitUsernames
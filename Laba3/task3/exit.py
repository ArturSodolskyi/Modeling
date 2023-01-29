import numpy as np
from element import Element


class Exit(Element):
    def __init__(self):
        super().__init__()
        self.tNext = np.inf
        self.finishedTimes = [0, 0, 0]
        self.typesCount = [0, 0, 0]

    def inAct(self, type, tStart):
        self.quantity += 1
        typeIndex = type - 1
        self.finishedTimes[typeIndex] += self.tCurrent - tStart
        self.typesCount[typeIndex] += 1

    def getTNext(self):
        return self.tNext

    def getMeanFinishedTime(self, type):
        typeIndex = type - 1
        typeCount = self.typesCount[typeIndex]
        if typeCount != 0:
            return self.finishedTimes[typeIndex] / typeCount
        else:
            return 0

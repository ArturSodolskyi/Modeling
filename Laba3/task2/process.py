import numpy as np
from element import Element
from processingItem import ProcessingItem


class Process(Element):
    def __init__(self):
        super().__init__()
        self.maxQueue = np.inf
        self.threads = 1
        self.queue = 0
        self.processingItems = []
        self.meanLoad = 0
        self.meanQueue = 0
        self.refusals = 0
        self.meanDepartureTime = 0
        self.previousDepartureTime = 0
        self.meanBankTime = 0
        self.previousBankTime = 0

    def inAct(self):
        if self.hasAvailableThreads():
            self.previousBankTime = self.tCurrent
            self.addToProcessing()
        elif self.queue < self.maxQueue:
            self.queue += 1
        else:
            self.refusals += 1

    def hasAvailableThreads(self):
        return len(self.processingItems) < self.threads

    def outAct(self):
        for item in self.getProcessedItems():
            super().outAct()
            self.processingItems.remove(item)

            self.meanDepartureTime += self.tCurrent - self.previousDepartureTime
            self.previousDepartureTime = self.tCurrent
            self.meanBankTime = + self.tCurrent - self.previousBankTime

            nextElement = self.getNextElement()
            if nextElement is not None:
                nextElement.inAct(self.tCurrent)

            if self.queue > 0:
                self.queue -= 1
                self.addToProcessing()

    def getProcessedItems(self):
        result = []
        for item in self.processingItems:
            if item.tNext == self.tCurrent:
                result.append(item)
        return result

    def addToProcessing(self):
        item = ProcessingItem()
        item.tNext = self.tCurrent + self.getDelay()
        self.processingItems.append(item)

    def doStatistics(self, delta):
        self.meanQueue += self.queue * delta
        self.meanLoad = (
            self.meanLoad + (len(self.processingItems) * delta)) / self.threads

    def getTNext(self):
        result = np.inf
        for item in self.processingItems:
            if item.tNext < result:
                result = item.tNext
        return result

    def printInfo(self):
        super().printInfo()
        print(f'{self.name}: failure = {self.failure}, queueLength = {self.queue}')

    def getRefusalsPercentage(self):
        return self.refusals / (self.quantity + len(self.processingItems))

    def getMeanDepartureTime(self):
        return self.meanDepartureTime / self.quantity

    def getMeanBankTime(self):
        return self.meanBankTime / self.quantity

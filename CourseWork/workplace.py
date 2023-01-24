from element import Element
from processingItem import ProcessingItem
from queueItem import QueueItem
import numpy as np


class Workplace(Element):
    # Середній час обслуговування для кожного типу робіт
    # та кожного завдання за дані в наступній таблиці:
    meanDelaysOfTypeAndWorkplacePairs = {
        1: {
            3: 0.5,
            1: 0.6,
            2: 0.85,
            5: 0.5
        },
        2: {
            4: 1.1,
            1: 0.8,
            3: 0.75
        },
        3: {
            2: 1.24,
            5: 0.25,
            1: 0.7,
            4: 0.9,
            3: 1.0
        }
    }

    def __init__(self):
        super().__init__()
        self.name = 'Workplace'
        self.queue = []
        self.processingItems = []
        self.machinesCount = 1
        self.meanLoad = 0

    def inAct(self, type, tStart):
        if self.hasAvailableMachine():
            self.addToProcessing(type, tStart)
        else:
            self.addToQueue(type, tStart)

    def hasAvailableMachine(self):
        return len(self.processingItems) < self.machinesCount

    def addToQueue(self, type, tStart):
        item = QueueItem()
        item.type = type
        item.tStart = tStart
        self.queue.append(item)

    def outAct(self):
        for item in self.getProcessedItems():
            super().outAct()
            self.totalTimeOfWork += self.tCurrent - item.tStart
            self.processingItems.remove(item)
            nextElement = self.getNextElement(item.type)
            if nextElement is not None:
                nextElement.inAct(item.type, self.tCurrent)

            if len(self.queue) > 0:
                # FIFO
                toAdd = self.queue.pop(0)
                self.totalWaitingTime += self.tCurrent - toAdd.tStart
                self.addToProcessing(toAdd.type, self.tCurrent)

    def getProcessedItems(self):
        result = []
        for item in self.processingItems:
            if item.tNext == self.tCurrent:
                result.append(item)
        return result

    def addToProcessing(self, type, tStart):
        item = ProcessingItem()
        item.type = type
        item.tStart = tStart
        item.tNext = self.tCurrent + self.getDelay(type)
        self.processingItems.append(item)

    def getDelay(self, type):
        self.delayMean = Workplace.meanDelaysOfTypeAndWorkplacePairs[type][self.workplaceNumber]
        return super().getDelay()

    def doStatistics(self, delta):
        self.meanLoad = (self.meanLoad + (len(self.processingItems) * delta)) / self.machinesCount

    def getTNext(self):
        result = np.inf
        for item in self.processingItems:
            if item.tNext < result:
                result = item.tNext
        return result

    def getMeanWaitingTime(self):
        return self.totalWaitingTime / (self.quantity + len(self.processingItems))

import numpy as np
from element import Element
from processingItem import ProcessingItem
from queueItem import QueueItem


class Process(Element):
    def __init__(self):
        super().__init__()
        self.maxQueue = np.inf
        self.threads = 1
        self.queue = []
        self.processingItems = []
        self.path = None
        self.timeToLaboratoryRegister = 0
        self.previousTimeToLaboratoryRegister = 0
        self.secondTypeFinishedTime = 0
        self.secondTypeCount = 0

    def inAct(self, type, tStart):
        if self.name == 'Way to the laboratory register':
            self.timeToLaboratoryRegister += self.tCurrent - self.previousTimeToLaboratoryRegister
            self.previousTimeToLaboratoryRegister = self.tCurrent

        if self.name == 'Way to the reception' and type == 2:
            self.secondTypeFinishedTime += self.tCurrent - tStart
            self.secondTypeCount += 1

        if self.hasAvailableThreads():
            self.addToProcessing(type, tStart)
        elif len(self.queue) < self.maxQueue:
            self.addToQueue(type, tStart)

    def hasAvailableThreads(self):
        return len(self.processingItems) < self.threads

    def addToQueue(self, type, tStart):
        item = QueueItem()
        item.type = type
        item.tStart = tStart
        self.queue.append(item)

    def outAct(self):
        for item in self.getProcessedItems():
            super().outAct()
            self.processingItems.remove(item)

            type = self.getTypeForNextElement(item.type)
            nextElement = self.getNextElement(type)
            if nextElement is not None:
                nextElement.inAct(type, item.tStart)

            if len(self.queue) > 0:
                toAdd = self.popFromQueue()
                self.addToProcessing(toAdd.type, self.tCurrent)

    def getTypeForNextElement(self, type):

        if self.name == 'Way to the reception':
            return 1
        else:
            return type

    def getNextElement(self, type):
        if self.path is None:
            return self.nextElements[0]
        else:
            for index, path in enumerate(self.path):
                if type in path:
                    return self.nextElements[index]

    def popFromQueue(self):
        index = self.getQueuePriorityIndex()
        return self.queue.pop(index)

    def getQueuePriorityIndex(self):
        for processingItem in self.processingItems:
            for queueItem in self.queue:
                if processingItem.type == queueItem.type:
                    return self.queue.index(queueItem)
        else:
            return 0

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

    def getTNext(self):
        result = np.inf
        for item in self.processingItems:
            if item.tNext < result:
                result = item.tNext
        return result

    def getDelay(self, type):
        if self.name == 'Reception':
            self.delayMean = Element.typeMeanDelays[type]
        return super().getDelay()

    def getSecondTypeMeanTime(self):
        if self.secondTypeCount != 0:
            return self.secondTypeFinishedTime / self.secondTypeCount
        else:
            return 0

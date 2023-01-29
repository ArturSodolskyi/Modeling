import numpy as np
from process import Process


class Model:
    def __init__(self, elements):
        self.list = elements
        self.tNext = 0
        self.tCurrent = self.tNext
        self.meanClientsCount = 0
        self.queueChangesCount = 0

    def simulate(self, time):
        while self.tCurrent < time:
            self.tNext = np.inf
            for item in self.list:
                tNextValue = item.getTNext()
                if tNextValue < self.tNext:
                    self.tNext = tNextValue

            for item in self.list:
                item.doStatistics(self.tNext - self.tCurrent)

            self.doStatistics(self.tNext - self.tCurrent)

            self.tCurrent = self.tNext

            for item in self.list:
                item.tCurrent = self.tCurrent

            for item in self.list:
                if self.tCurrent == item.getTNext():
                    item.outAct()

            self.changeQueueIfPossible()

        self.printResult()
        self.printTotalResult()

    def doStatistics(self, delta):
        sumOfQueues = 0
        sumOfWindowsClients = 0
        for e in self.list:
            if isinstance(e, Process):
                sumOfQueues += e.queue
                sumOfWindowsClients += len(e.processingItems)
        self.meanClientsCount += (sumOfQueues + sumOfWindowsClients) * delta

    def changeQueueIfPossible(self):
        firstQueue = self.list[1].queue
        secondQueue = self.list[2].queue
        if firstQueue - secondQueue >= 2:
            self.list[1].queue -= 1
            self.list[2].queue += 1
            print("Car From The First Queue Changed Queue")
            self.queueChangesCount += 1
        elif secondQueue - secondQueue >= 2:
            self.list[2].queue -= 1
            self.list[1].queue += 1
            print("Car From The Second Queue Changed Queue")
            self.queueChangesCount += 1

    def printResult(self):
        print()
        print('Result:')

        for e in self.list:
            if isinstance(e, Process):
                e.printResult()
                print(f"Average Queue Length: {self.getMeanQueueLength(e)}")
                print(f"Average Load: {self.getMeanLoad(e)}")
                print()

    def printTotalResult(self):
        print()
        print('Total result:')

        processCount = 0
        meanDepartureTimeSum = 0
        meanBankTimeSum = 0
        refusalsPercentageSum = 0
        for e in self.list:
            if isinstance(e, Process):
                processCount += 1
                meanDepartureTimeSum += e.getMeanDepartureTime()
                meanBankTimeSum += e.getMeanBankTime()
                refusalsPercentageSum += e.getRefusalsPercentage()

        meanDepartureTime = meanDepartureTimeSum / processCount
        meanBankTime = meanBankTimeSum / processCount
        meanClientsCount = self.getMeanClientsCount()
        meanRefusalsPercentage = refusalsPercentageSum / processCount

        print(f"Average Departure Time: {meanDepartureTime}")
        print(f"Average Clients Time In Bank: {meanBankTime}")
        print(f"Average Clients Count: {meanClientsCount}")
        print(f"Refusals Percentage: {meanRefusalsPercentage}")
        print(f"Queue Changes Count: {self.queueChangesCount}")
        print()

    def getMeanClientsCount(self):
        return self.meanClientsCount / self.tCurrent

    def getMeanLoad(self, e: Process):
        return e.meanLoad / self.tCurrent

    def getMeanQueueLength(self, e: Process):
        return e.meanQueue / self.tCurrent

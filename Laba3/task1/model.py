import numpy as np
from process import Process


class Model:
    def __init__(self, elements):
        self.list = elements
        self.tNext = 0
        self.tCurrent = self.tNext

    def simulate(self, time):
        while self.tCurrent < time:
            self.tNext = np.inf
            for item in self.list:
                tNextValue = item.getTNext()
                if tNextValue < self.tNext:
                    self.tNext = tNextValue

            for item in self.list:
                item.doStatistics(self.tNext - self.tCurrent)

            self.tCurrent = self.tNext

            for item in self.list:
                item.tCurrent = self.tCurrent

            for item in self.list:
                if self.tCurrent == item.getTNext():
                    item.outAct()

        self.printResult()
        self.printTotalResult()

    def printResult(self):
        print()
        print('Result:')

        for e in self.list:
            if isinstance(e, Process):
                e.printResult()
                print(f"Average Queue Length: {self.getMeanQueueLength(e)}")
                print(f"Failure Probability: {self.getFailureProbability(e)}")
                print(f"Average Load: {self.getMeanLoad(e)}")
                print()

    def printTotalResult(self):
        print()
        print('Total result:')

        meanQueueLengthSum = 0
        failureProbabilitySum = 0
        meanLoadSum = 0
        processorsCount = 0
        for e in self.list:
            if isinstance(e, Process):
                processorsCount += 1
                meanQueueLengthSum += self.getMeanQueueLength(e)
                failureProbabilitySum += self.getFailureProbability(e)
                meanLoadSum += self.getMeanLoad(e)

        meanQueueLengthResult = meanQueueLengthSum / processorsCount
        failureProbabilityResult = failureProbabilitySum / processorsCount
        meanLoadResult = meanLoadSum / processorsCount

        print(f"Average Queue Length: {meanQueueLengthResult}")
        print(f"Failure Probability: {failureProbabilityResult}")
        print(f"Average Load: {meanLoadResult}")
        print()

    def getFailureProbability(self, e: Process):
        return e.failure / (e.quantity + e.failure) if (e.quantity + e.failure) != 0 else 0

    def getMeanLoad(self, e: Process):
        return e.meanLoad / self.tCurrent

    def getMeanQueueLength(self, e: Process):
        return e.meanQueue / self.tCurrent

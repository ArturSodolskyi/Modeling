import numpy as np
from workplace import Workplace


class Model:
    def __init__(self, elements):
        self.list = elements
        self.tNext = 0.0
        self.tCurrent = self.tNext

    def simulate(self, time, onlyTotalResults=False):
        while self.tCurrent < time:
            self.tNext = np.inf
            for item in self.list:
                tNextValue = np.min(item.getTNext())
                if tNextValue < self.tNext:
                    self.tNext = tNextValue

            for item in self.list:
                item.doStatistics(self.tNext - self.tCurrent)

            self.tCurrent = self.tNext

            for item in self.list:
                item.tCurrent = self.tCurrent
                if self.tCurrent == item.getTNext():
                    item.outAct()
        self.printResult(onlyTotalResults)

    def printResult(self, onlyTotalResults):
        print()
        print('Results:')

        processorsCount = 0
        totalWaitingTime = 0
        totalTimeOfWork = 0
        meanLoadSum = 0
        for e in self.list:
            if isinstance(e, Workplace):
                processorsCount += 1

                waitingTime = e.getMeanWaitingTime()
                timeOfWork = e.getMeanTimeOfWork()
                meanLoad = self.getMeanLoad(e)
                if onlyTotalResults is False:
                    e.printResult()
                    self.printData(waitingTime, timeOfWork, meanLoad)

                totalWaitingTime += waitingTime
                totalTimeOfWork += timeOfWork
                meanLoadSum += meanLoad

        # В обрахунок також входять ті процеси, які не стояли в черзі,
        # тобто їх час очікування дорівнював 0
        meanWaitingTime = totalWaitingTime / processorsCount
        meanTimeOfWork = totalTimeOfWork / processorsCount
        meanLoadResult = meanLoadSum / processorsCount

        print("Total Results:")

        # Визначити середній час, витрачений роботами на очікування;
        # середній час виконання роботи;
        # коефіцієнти завантаження робочих місць.
        self.printData(meanWaitingTime, meanTimeOfWork, meanLoadResult)

    def printData(self, waitingTime, timeOfWork, meanLoad):
        print(f"Average Waiting Time: {waitingTime}")
        print(f"Average Time of Work: {timeOfWork}")
        print(f"Average Load: {meanLoad}")
        print()

    def getMeanLoad(self, e: Workplace):
        return e.meanLoad / self.tCurrent
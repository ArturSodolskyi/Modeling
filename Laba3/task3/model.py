import numpy as np
from process import Process
from exit import Exit


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
        print('Results:')
        print()

        processes = self.filter(lambda item: isinstance(item, Process))

        for e in processes:
            if e.name == 'Way to the reception':
                print(f'{e.name}:')
                print(
                    f'Type 2 Average Time To Finish = {e.getSecondTypeMeanTime()}')

        print()

        exits = self.filter(lambda item: isinstance(item, Exit))
        for e in exits:
            print(f'{e.name}:')
            print(
                f'Type 1 Average Time To Finish = {e.getMeanFinishedTime(1)}')
            print(
                f'Type 2 Average Time To Finish = {e.getMeanFinishedTime(2)}')
            print(
                f'Type 3 Average Time To Finish = {e.getMeanFinishedTime(3)}')
            print()

    def printTotalResult(self):
        print('Total Results:')
        print()

        processes = self.filter(lambda item: isinstance(item, Process))
        exits = self.filter(lambda item: isinstance(item, Exit))

        processCount = 0
        laboratoryRegisterIntervalSum = 0
        for process in processes:
            processCount += 1
            if process.name == 'Way to the laboratory register':
                laboratoryRegisterIntervalSum += process.timeToLaboratoryRegister / process.quantity

        finishedTimeSum = 0
        finishedCount = 0
        for exit in exits:
            finishedTimeSum += sum(exit.finishedTimes)
            finishedCount += exit.quantity

        laboratoryRegisterIntervalMean = laboratoryRegisterIntervalSum
        finishedTimeMean = finishedTimeSum / finishedCount

        print(f'Average Interval To Laboratory Register: {laboratoryRegisterIntervalMean}')
        print(f'Average Time To Finish: {finishedTimeMean}')
        print()

    def filter(self, function):
        return filter(function, self.list)

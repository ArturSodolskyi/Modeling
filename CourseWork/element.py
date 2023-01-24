import funRand


class Element:
    # Для робіт 1, 2 та 3 потрібно виконання
    # 4, 3 та 5 завдань відповідно.
    # Для різних типів робіт використовуються
    # наступні технологічні маршрути:
    typesExecutionPlan = {
        1: [3, 1, 2, 5],
        2: [4, 1, 3],
        3: [2, 5, 1, 4, 3]
    }

    def __init__(self, delay=None, distribution=None):
        self.name = ''
        self.distribution = distribution
        self.delayMean = delay
        self.delayDev = None
        self.tCurrent = 0
        self.nextElements = None
        self.quantity = 0
        self.workplaceNumber = None
        self.totalWaitingTime = 0
        self.totalTimeOfWork = 0

    def getDelay(self):
        if 'exp' == self.distribution:
            return funRand.exponential(self.delayMean)
        elif 'norm' == self.distribution:
            return funRand.normal(self.delayMean, self.delayDev)
        elif 'uniform' == self.distribution:
            return funRand.uniform(self.delayMean, self.delayDev)
        elif 'erlang' == self.distribution:
            return funRand.erlang(self.delayMean, self.delayDev)
        else:
            return self.delayMean

    def inAct(self, type, tStart):
        pass

    def outAct(self):
        self.quantity += 1

    def doStatistics(self, delta):
        pass

    def getNextElement(self, type):
        executionPlan = Element.typesExecutionPlan[type]
        if len(executionPlan) == 0:
            raise ValueError('Cannot find type execution plan.')
        if self.workplaceNumber is None:
            workplaceNumber = executionPlan[0]
            return Element.getNextElementByWorkplaceNumber(self, workplaceNumber)
        index = executionPlan.index(self.workplaceNumber)
        if index == len(executionPlan) - 1:
            return None
        workplaceNumber = executionPlan[index + 1]
        return Element.getNextElementByWorkplaceNumber(self, workplaceNumber)

    def getNextElementByWorkplaceNumber(self, workplaceNumber):
        for item in self.nextElements:
            if item.workplaceNumber == workplaceNumber:
                return item

    def getTNext():
        pass

    def getMeanWaitingTime(self):
        return self.totalWaitingTime / self.quantity

    def getMeanTimeOfWork(self):
        return self.totalTimeOfWork / self.quantity

    def printResult(self):
        print(f'{self.name} {self.workplaceNumber}: quantity = {self.quantity}')

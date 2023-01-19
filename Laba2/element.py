import funRand

class Element:
    nextId = 0

    def __init__(self, delay = None, distribution = None):
        self.tNext = [0]
        self.delayMean = delay
        self.distribution = distribution
        self.tCurrent = self.tNext
        self.state = [0]
        self.nextElement = None
        self.id = Element.nextId
        Element.nextId += 1
        self.name = f'element {self.id}'
        self.delayDev = None
        self.quantity = 0
        self.probability = [1]

    def getDelay(self):
        if 'exp' == self.distribution:
            return funRand.exponential(self.delayMean)
        elif 'norm' == self.distribution:
            return funRand.normal(self.delayMean, self.delayDev)
        elif 'uniform' == self.distribution:
            return funRand.uniform(self.delayMean, self.delayDev)
        else:
            return self.delayMean

    def inAct(self):
        pass

    def outAct(self):
        self.quantity += 1

    def printResult(self):
        print(f'{self.name} quantity = {self.quantity}, state = {self.state}')

    def printInfo(self):
        print(f'{self.name} state = {self.state}, quantity = {self.quantity}, tNext = {self.tNext}')

    def doStatistics(self, delta):
        pass

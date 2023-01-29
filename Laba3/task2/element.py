import funRand as funRand


class Element:
    def __init__(self, delay=None, distribution=None):
        self.name = ''
        self.distribution = distribution
        self.delayMean = delay
        self.delayDev = None
        self.tCurrent = 0
        self.nextElements = []
        self.quantity = 0

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

    def getNextElement(self):
        if len(self.nextElements) > 0:
            return self.nextElements[0]
        else:
            return None

    def printResult(self):
        print(f'{self.name} - quantity = {self.quantity}')

    def inAct(self):
        pass

    def outAct(self):
        self.quantity += 1

    def doStatistics(self, delta):
        pass

    def getTNext():
        pass

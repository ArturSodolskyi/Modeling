import funRand as funRand
import numpy as np


class Element:
    def __init__(self, delay=None, distribution=None):
        self.name = ''
        self.distribution = distribution
        self.delayMean = delay
        self.delayDev = None
        self.tCurrent = 0
        self.nextElements = []
        self.quantity = 0
        self.isProbability = False
        self.isPriority = False

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
        if self.isProbability:
            return self.getNextElementByProbability()
        elif self.isPriority:
            return self.getNextElementByPriority()
        elif len(self.nextElements) > 0:
            return self.nextElements[0].element
        else:
            None

    def getNextElementByProbability(self):
        nextElements = []
        probabilities = []
        for item in self.nextElements:
            nextElements.append(item.element)
            probabilities.append(item.probability)

        return np.random.choice(a=nextElements, p=probabilities)

    def getNextElementByPriority(self):
        priorities = []
        for item in self.nextElements:
            priorities.append(item.priority)

        minQueueLength = np.inf
        minQueueLengthIndex = 0
        for e in range(len(priorities)):
            maxPriority = max(priorities)
            if maxPriority == -1:
                break

            maxPriorityIndex = priorities.index(maxPriority)
            nextElement = self.nextElements[maxPriorityIndex]
            if len(nextElement.element.processingItems) < nextElement.element.threads:
                return nextElement.element
            elif nextElement.element.queue < minQueueLength:
                minQueueLength = nextElement.element.queue
                minQueueLengthIndex = self.nextElements.index(nextElement)

            priorities[maxPriorityIndex] = -1

        return self.nextElements[minQueueLengthIndex].element

    def printResult(self):
        print(f'{self.name} - quantity = {str(self.quantity)}')

    def inAct(self):
        pass

    def outAct(self):
        self.quantity += 1

    def doStatistics(self, delta):
        pass

    def getTNext():
        pass

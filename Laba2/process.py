import numpy as np
from element import Element

class Process(Element):
    def __init__(self, delay, threads = 1):
        super().__init__(delay)
        self.queue = 0
        self.maxQueue = float('inf')
        self.meanQueue = 0.0
        self.failure = 0
        self.threads = threads
        self.tNext = [np.inf] * self.threads
        self.state = [0] * self.threads
        self.probability = [1]
        self.meanLoad = 0

    def inAct(self):        
        availableThreads = self.getAvailableThreads()
        if len(availableThreads) > 0:
            for i in availableThreads:
                self.state[i] = 1
                self.tNext[i] = self.tCurrent + super().getDelay()
                break
        else:
            if self.queue < self.maxQueue:
                self.queue += 1
            else:
                self.failure += 1

    def outAct(self):
        currentThreads = self.getCurrentThreads()
        for i in currentThreads:
            super().outAct()
            self.tNext[i] = np.inf
            self.state[i] = 0
            if self.queue > 0:
                self.queue -= 1
                self.state[i] = 1
                self.tNext[i] = self.tCurrent + self.getDelay()
            if self.nextElement is not None:
                next_el = np.random.choice(a = self.nextElement, p = self.probability)
                next_el.inAct()
    
    def printInfo(self):
        super().printInfo()
        print(f'{self.name}: failure = {self.failure}, queueLength = {self.queue}')

    def doStatistics(self, delta):
        self.meanQueue += self.queue * delta
        for i in range(self.threads):
            self.meanLoad += self.state[i] * delta
        self.meanLoad /= self.threads

    def getAvailableThreads(self):
        result = []
        for i in range(self.threads):
            if self.state[i] == 0:
                result.append(i)
        return result

    def getCurrentThreads(self):
        result = []
        for i in range(self.threads):
            if self.tNext[i] == self.tCurrent:
                result.append(i)
        return result
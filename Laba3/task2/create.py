from element import Element


class Create(Element):
    def __init__(self):
        super().__init__()
        self.tNext = 0

    def outAct(self):
        super().outAct()
        self.tNext = self.tCurrent + self.getDelay()
        self.getNextElement().inAct()

    def getNextElement(self):
        firstElement = self.nextElements[0]
        secondElement = self.nextElements[1]
        if (firstElement.queue == secondElement.queue) or (firstElement.queue < secondElement.queue):
            return firstElement
        else:
            return secondElement

    def getTNext(self):
        return self.tNext

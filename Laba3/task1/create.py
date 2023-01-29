from element import Element


class Create(Element):
    def __init__(self):
        super().__init__()
        self.tNext = 0

    def outAct(self):
        super().outAct()
        self.tNext = self.tCurrent + self.getDelay()
        nextElement = self.getNextElement()
        if nextElement is not None:
            nextElement.inAct()

    def getTNext(self):
        return self.tNext

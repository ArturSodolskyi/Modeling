import numpy as np
from element import Element


class Create(Element):
    def __init__(self):
        super().__init__()
        self.tNext = 0

    def outAct(self):
        super().outAct()
        self.tNext = self.tCurrent + self.getDelay()
        type = np.random.choice([1, 2, 3], p=[0.5, 0.1, 0.4])
        self.getNextElement().inAct(type, self.tCurrent)

    def getTNext(self):
        return self.tNext

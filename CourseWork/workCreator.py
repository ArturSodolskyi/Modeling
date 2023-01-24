import numpy as np
from element import Element


class WorkCreator(Element):
    def __init__(self):
        super().__init__()
        self.name = 'Work Creator'
        self.tNext = 0

    def outAct(self):
        super().outAct()
        self.tNext = self.tCurrent + self.getDelay()

        # Існує три типи робіт: 1,2 і 3, 
        # що виникають із ймовірностями 0,3, 0,5 і 0,2.
        type = np.random.choice([1, 2, 3], p=[0.3, 0.5, 0.2])

        nextElement = self.getNextElement(type)
        if nextElement is not None:
            nextElement.inAct(type, self.tCurrent)
        else:
            raise ValueError('Invalid type.')

    def getTNext(self):
        return self.tNext

import numpy as np


class ProcessingItem:
    def __init__(self):
        self.tStart = np.inf
        self.tNext = np.inf
        self.type = None

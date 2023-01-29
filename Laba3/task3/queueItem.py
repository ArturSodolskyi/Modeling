import numpy as np


class QueueItem:
    def __init__(self):
        self.tStart = np.inf
        self.type = None

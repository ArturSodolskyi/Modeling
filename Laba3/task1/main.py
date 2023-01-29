from create import Create
from model import Model
from nextElement import NextElement
from process import Process


def mainForProbability():
    p1 = Process()
    p1.name = 'Process 1'
    p1.maxQueue = 2
    p1.delayMean = 3
    p1.distribution = 'exp'
    p1.threads = 4

    p2 = Process()
    p2.name = 'Process 2'
    p2.maxQueue = 2
    p2.delayMean = 3
    p2.distribution = 'exp'
    p2.threads = 4

    c = Create()
    c.name = 'Creator'
    c.delayMean = 1
    c.distribution = 'exp'
    c.isProbability = True

    nextElement1 = NextElement()
    nextElement1.element = p1
    nextElement1.probability = 0.6

    nextElement2 = NextElement()
    nextElement2.element = p2
    nextElement2.probability = 0.4

    c.nextElements = [nextElement1, nextElement2]

    elements = [c, p1, p2]
    model = Model(elements)
    model.simulate(1000)


def mainForPriority():
    p1 = Process()
    p1.name = 'Process 1'
    p1.maxQueue = 2
    p1.delayMean = 3
    p1.distribution = 'exp'
    p1.threads = 4

    p2 = Process()
    p2.name = 'Process 2'
    p2.maxQueue = 2
    p2.delayMean = 3
    p2.distribution = 'exp'
    p2.threads = 4

    c = Create()
    c.name = 'Creator'
    c.delayMean = 1
    c.distribution = 'exp'
    c.isPriority = True

    nextElement1 = NextElement()
    nextElement1.element = p1
    nextElement1.priority = 2

    nextElement2 = NextElement()
    nextElement2.element = p2
    nextElement2.priority = 1

    c.nextElements = [nextElement1, nextElement2]

    elements = [c, p1, p2]
    model = Model(elements)
    model.simulate(1000)


if __name__ == "__main__":
    # mainForProbability()
    mainForPriority()

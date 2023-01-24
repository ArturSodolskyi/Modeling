from workCreator import WorkCreator
from model import Model
from workplace import Workplace


def main():
    # Роботи надходять у систему з інтервалами,
    # що є незалежними величинами, що розподілені за експоненціальним законом
    # із середнім значенням 0,25 години.
    creator = WorkCreator()
    creator.distribution = 'exp'
    creator.delayMean = 0.25

    # Виробнича система складається з п’яти
    # автоматизованих робочих місць.
    w1 = Workplace()
    w1.workplaceNumber = 1

    w2 = Workplace()
    w2.workplaceNumber = 2

    w3 = Workplace()
    w3.workplaceNumber = 3

    w4 = Workplace()
    w4.workplaceNumber = 4

    w5 = Workplace()
    w5.workplaceNumber = 5

    # На теперішній момент міста 1,2,3,4,5
    # включають відповідно 3,2,4,3 і 1 однакових станків.
    w1.machinesCount = 3
    w2.machinesCount = 2
    w3.machinesCount = 4
    w4.machinesCount = 3
    w5.machinesCount = 1

    # Час виконання завдання на кожному станку є незалежною
    # випадковою величиною, що має закон розподілу
    # Ерланга 2-ого порядку із середнім значенням, що залежить від типу
    # роботи та від робочого місця, за яким закріплений станок.
    w1.distribution = 'erlang'
    w2.distribution = 'erlang'
    w3.distribution = 'erlang'
    w4.distribution = 'erlang'
    w5.distribution = 'erlang'

    w1.delayDev = 2
    w2.delayDev = 2
    w3.delayDev = 2
    w4.delayDev = 2
    w5.delayDev = 2

    creator.nextElements = [w1, w2, w3, w4, w5]
    w1.nextElements = [w2, w3, w4, w5]
    w2.nextElements = [w1, w3, w4, w5]
    w3.nextElements = [w1, w2, w4, w5]
    w4.nextElements = [w1, w2, w3, w5]
    w5.nextElements = [w1, w2, w3, w4]

    model = Model([creator, w1, w2, w3, w4, w5])
    model.simulate(1000)

def mainForExperiment():
    inputData = [
        [0.1, 1],
        [0.5, 1],
        [0.1, 5],
        [0.5, 5]
    ]

    for data in inputData:
        delayMean = data[0]
        machinesCount = data[1]
        print(f'delayMean={delayMean}, machinesCount={machinesCount}')
        initForExperiment(delayMean, machinesCount)

def initForExperiment(delayMean, machinesCount):
    creator = WorkCreator()
    creator.distribution = 'exp'
    creator.delayMean = delayMean
    w1 = Workplace()
    w1.workplaceNumber = 1
    w2 = Workplace()
    w2.workplaceNumber = 2
    w3 = Workplace()
    w3.workplaceNumber = 3
    w4 = Workplace()
    w4.workplaceNumber = 4
    w5 = Workplace()
    w5.workplaceNumber = 5
    w1.machinesCount = machinesCount
    w2.machinesCount = machinesCount
    w3.machinesCount = machinesCount
    w4.machinesCount = machinesCount
    w5.machinesCount = machinesCount
    w1.distribution = 'erlang'
    w2.distribution = 'erlang'
    w3.distribution = 'erlang'
    w4.distribution = 'erlang'
    w5.distribution = 'erlang'
    w1.delayDev = 2
    w2.delayDev = 2
    w3.delayDev = 2
    w4.delayDev = 2
    w5.delayDev = 2
    creator.nextElements = [w1, w2, w3, w4, w5]
    w1.nextElements = [w2, w3, w4, w5]
    w2.nextElements = [w1, w3, w4, w5]
    w3.nextElements = [w1, w2, w4, w5]
    w4.nextElements = [w1, w2, w3, w5]
    w5.nextElements = [w1, w2, w3, w4]
    model = Model([creator, w1, w2, w3, w4, w5])
    model.simulate(1000, True)


if __name__ == "__main__":
    main()
    # mainForExperiment()

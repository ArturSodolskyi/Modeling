from create import Create
from model import Model
from process import Process
from funRand import normal
from processingItem import ProcessingItem


def main():
    # Тривалість обслуговування в обох касирів однакова 
    # і розподілена експоненційно з математичним 
    # очікуванням, рівним 0,3 од. часу
    p1 = Process()
    p1.name = 'Service Window 1'
    p1.distribution = 'exp'
    p1.delayMean = 0.3
    p1.maxQueue = 3

    p2 = Process()
    p2.name = 'Service Window 2'
    p2.distribution = 'exp'
    p2.delayMean = 0.3
    p2.maxQueue = 3

    # обидва касири зайняті, тривалість
    # обслуговування для кожного касира нормально розподілена з
    # математичним очікуванням, рівним 1 од. часу, і середньоквадратичним
    # відхиленням, рівним 0,3 од. часу
    item1 = ProcessingItem()
    item1.tNext = normal(1, 0.3)
    p1.processingItems.append(item1)

    item2 = ProcessingItem()
    item2.tNext = normal(1, 0.3)
    p2.processingItems.append(item2)

    # У кожній черзі очікують по два автомобіля
    p1.queue = 2
    p2.queue = 2

    c = Create()
    c.name = 'Creator'
    # інтервали часу між прибуттям клієнтів у 
    # годину пік розподілені експоненційно з
    # математичним очікуванням, рівним 0,5 од. часу
    c.distribution = 'exp'
    c.delayMean = 0.5
    c.nextElements = [p1, p2]

    # прибуття першого клієнта
    # заплановано на момент часу 0,1 од. часу
    c.tNext = 0.1

    elements = [c, p1, p2]
    model = Model(elements)
    model.simulate(1000)


if __name__ == "__main__":
    main()

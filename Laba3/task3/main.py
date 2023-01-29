from create import Create
from model import Model
from process import Process
from exit import Exit
import numpy as np


def main():
    creator = Create()
    creator.name = 'Creator'
    # Час між прибуттями в приймальне
    # відділення - Експоненціальний з
    # математичним сподіванням 15
    creator.delayMean = 15
    creator.distribution = 'exp'

    reception = Process()
    reception.name = 'Reception'
    #При надходженні в приймальне відділення хворий стає в чергу,
    # якщо обидва чергових лікарі зайняті
    reception.threads = 2

    wardWay = Process()
    wardWay.name = 'Way to the ward'
    # Час слідування в палату -
    # Рівномірне від 3 до 8
    wardWay.distribution = 'uniform'
    wardWay.delayMean = 3
    wardWay.delayDev = 8
    # Троє супровідних розводять хворих по палатах
    wardWay.threads = 3

    laboratoryRegisterWay = Process()
    laboratoryRegisterWay.name = 'Way to the laboratory register'
    # Хворі, що спрямовуються в лабораторію, не потребують супроводу.
    laboratoryRegisterWay.threads = np.inf

    receptionWay = Process()
    receptionWay.name = 'Way to the reception'
    receptionWay.threads = np.inf

    # Час слідування з приймального
    # відділення в лабораторію або з
    # лабораторії в приймальне відділення - 
    # Рівномірне від 2 до 5
    laboratoryRegisterWay.distribution = 'uniform'
    laboratoryRegisterWay.delayMean = 2
    laboratoryRegisterWay.delayDev = 5

    receptionWay.distribution = 'uniform'
    receptionWay.delayMean = 2
    receptionWay.delayDev = 5

    laboratoryRegistrationService = Process()
    laboratoryRegistrationService.name = 'Service in the laboratory register'
    # Час обслуговування в реєстратуру
    # лабораторії - Ерланга з математичним
    # сподіванням 4,5 і k=3
    laboratoryRegistrationService.delayMean = 4.5
    laboratoryRegistrationService.delayDev = 3
    laboratoryRegistrationService.threads = 1
    laboratoryRegistrationService.distribution = 'erlang'

    laboratoryAnalysis = Process()
    laboratoryAnalysis.name = 'Analysis in the laboratory'
    # Час проведення аналізу в лабораторії -
    # Ерланга з математичним сподіванням 4 і k=2
    laboratoryAnalysis.delayMean = 4
    laboratoryAnalysis.delayDev = 2
    laboratoryAnalysis.threads = 2
    laboratoryAnalysis.distribution = 'erlang'

    exit = Exit()
    exit.name = 'Exit'

    creator.nextElements = [reception]
    reception.nextElements = [wardWay, laboratoryRegisterWay]
    wardWay.nextElements = [exit]
    laboratoryRegisterWay.nextElements = [laboratoryRegistrationService]
    laboratoryRegistrationService.nextElements = [laboratoryAnalysis]
    laboratoryAnalysis.nextElements = [exit, receptionWay]
    receptionWay.nextElements = [reception]

    reception.path = [[1], [2, 3]]
    laboratoryAnalysis.path = [[3], [2]]

    elements = [creator, reception, wardWay,
                laboratoryRegisterWay, laboratoryAnalysis, 
                laboratoryRegistrationService, receptionWay, exit]
    model = Model(elements)
    model.simulate(1000)


if __name__ == "__main__":
    main()

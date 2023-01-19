import pandas as pd
from create import Create
from model import Model
from process import Process

class Sim():
    def task1(self):
        process = Process(5)
        process.maxQueue = 5
        process.distribution = 'exp'
        process.name = 'Process'

        creator = Create(5)
        creator.name = 'Creator'
        creator.distribution = 'exp'
        creator.nextElement = [process]

        model = Model([creator, process])
        model.simulate(1000)

    def task3(self):
        creator = Create(5)
        creator.name = 'Creator'
        creator.distribution = 'exp'

        p1 = Process(5)
        p1.maxQueue = 5
        p1.name = 'Process 1'
        p1.distribution = 'exp'

        p2 = Process(5)
        p2.maxQueue = 5
        p2.name = 'Process 2'
        p2.distribution = 'exp'

        p3 = Process(5)
        p3.maxQueue = 5
        p3.name = 'Process 3'
        p3.distribution = 'exp'

        creator.nextElement = [p1]
        p1.nextElement = [p2]
        p2.nextElement = [p3]
        
        model = Model([creator, p1, p2, p3])
        model.simulate(1000)

    def task4(self):
        creatorDelays = [16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8]
        processDelays = [
            [8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8],
            [8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8],
            [8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8],
        ]
        maxQueueValues = [
            [4, 4, 4, 4, 16, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 16, 4, 4, 1, 4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4, 16, 1, 4, 4, 4, 4, 4, 4, 4],
        ]
        distribution = 'exp'

        data = []
        for i in range(len(creatorDelays)):
            process3 = Process(processDelays[2][i])
            process3.name = 'Process 3'
            process3.distribution = distribution
            process3.maxQueue = maxQueueValues[2][i]

            process2 = Process(processDelays[1][i])
            process2.name = 'Process 2'
            process2.distribution = distribution
            process2.maxQueue = maxQueueValues[1][i]
            process2.nextElement = [process3]

            process1 = Process(processDelays[0][i])
            process1.name = 'Process 1'
            process1.distribution = distribution
            process1.maxQueue = maxQueueValues[0][i]
            process1.nextElement = [process2]

            creator = Create(creatorDelays[i])
            creator.name = 'Creator'
            creator.distribution = distribution
            creator.nextElement = [process1]

            model = Model([creator, process1, process2, process3])
            model.simulate(1000)

            data.append([
                creatorDelays[i],                  
                processDelays[0][i],
                processDelays[1][i],
                processDelays[2][i],
                maxQueueValues[0][i],
                maxQueueValues[1][i],
                maxQueueValues[2][i],
                process1.quantity,
                process1.failure,
                process2.quantity,
                process2.failure,
                process3.quantity,
                process3.failure
            ])

        columns = [
            'Creator Delay',
            'Process Delay 1',
            'Process Delay 2',
            'Process Delay 3',
            'Max Queue 1',
            'Max Queue 2',
            'Max Queue 3',
            'Process 1 - Success',
            'Process 1 - Fail',
            'Process 2 - Success',
            'Process 2 - Fail',
            'Process 3 - Success',
            'Process 3 - Fail'
            ]

        df = pd.DataFrame(data, columns = columns)
        pd.set_option('display.max_columns', None)
        print(f"Distribution: {distribution}")
        print(df)
        #'pip install openpyxl' to use df.to_excel
        # df.to_excel('verificationResults.xlsx')

    def task5And6(self):
        process = Process(5, 2)
        process.name = 'Process 1'
        process.distribution = 'exp'
        process.maxQueue = 5

        creator = Create(5)
        creator.name = 'Creator'
        creator.distribution = 'exp'
        creator.nextElement = [process]

        model = Model([creator, process])
        model.simulate(1000)
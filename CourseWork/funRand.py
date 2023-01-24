import random
import numpy as np


def exponential(timeMean):
    result = 0.0
    while result == 0:
        result = random.random()
    result = -timeMean * np.log(result)
    return result


def uniform(timeMin, timeMax):
    result = 0.0
    while result == 0:
        result = random.random()
    result = timeMin + result * (timeMax - timeMin)
    return result


def normal(timeMean, timeDeviation):
    return timeMean + timeDeviation * random.gauss(0.0, 1.0)


def erlang(time_mean, k):
    a = 1
    for i in range(k):
        a *= random.random()
    return - np.log(a) / (k * time_mean)

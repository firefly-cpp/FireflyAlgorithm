import numpy as np
from fireflyalgorithm import FireflyAlgorithm


def sphere(x):
    return np.sum(x ** 2)


FA = FireflyAlgorithm()
best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)

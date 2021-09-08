import numpy as np
from FireflyAlgorithm import FireflyAlgorithm


def sphere(x):
    return np.sum(x ** 2)


best = FireflyAlgorithm(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)

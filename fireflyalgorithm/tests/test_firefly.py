from unittest import TestCase

import numpy as np
from fireflyalgorithm import FireflyAlgorithm
import os

def sphere(x):
    return np.sum(x ** 2)

class TestFA(TestCase):
    def test_algorithm(self):
        FA = FireflyAlgorithm()
        best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)
        self.assertLess(best, 5)

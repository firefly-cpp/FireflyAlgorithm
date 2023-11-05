from unittest import TestCase
from fireflyalgorithm import FireflyAlgorithm
from fireflyalgorithm.problems import sphere


class TestFA(TestCase):
    def test_algorithm(self):
        algorithm = FireflyAlgorithm()
        best = algorithm.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)
        self.assertLess(best, 5)

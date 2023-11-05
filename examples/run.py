from fireflyalgorithm import FireflyAlgorithm
from fireflyalgorithm.problems import sphere


FA = FireflyAlgorithm()
best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)

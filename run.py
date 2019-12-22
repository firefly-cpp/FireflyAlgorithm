from FireflyAlgorithm import *


def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val


Algorithm = FireflyAlgorithm(10, 20, 10000, 0.5, 0.2, 1.0, -2.0, 2.0, Fun)
Best = Algorithm.Run()

print (Best)

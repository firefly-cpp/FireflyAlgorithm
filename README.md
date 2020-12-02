# Firefly Algorithm in Python

## INSTALLATION:

```sh
pip install FireflyAlgorithm
```
To install FireflyAlgorithm on Fedora, use:
```sh
$ dnf install python-FireflyAlgorithm
```

## CODE EXAMPLE:

```python
from FireflyAlgorithm import *


def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val


Algorithm = FireflyAlgorithm(10, 20, 10000, 0.5, 0.2, 1.0, -2.0, 2.0, Fun)
Best = Algorithm.Run()

print Best
```

## Reference Papers:

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds. 
Jozef Stefan Institute, Ljubljana, Slovenia, 2012 

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.

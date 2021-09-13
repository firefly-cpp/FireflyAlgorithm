# Firefly Algorithm in Python

## INSTALLATION:

```sh
pip install fireflyalgorithm
```
To install FireflyAlgorithm on Fedora, use:
```sh
$ dnf install python-fireflyalgorithm
```

## CODE EXAMPLE:

```python
from FireflyAlgorithm import *


def sphere(x):
    return np.sum(x ** 2)


best = FireflyAlgorithm(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)
print(best)
```

## Reference Papers:

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds. 
Jozef Stefan Institute, Ljubljana, Slovenia, 2012 

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.

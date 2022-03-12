# Firefly Algorithm --- Implementation of Firefly algorithm in Python

---

[![PyPI Version](https://img.shields.io/pypi/v/fireflyalgorithm.svg)](https://pypi.python.org/pypi/fireflyalgorithm)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fireflyalgorithm.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fireflyalgorithm.svg)
[![Downloads](https://pepy.tech/badge/fireflyalgorithm)](https://pepy.tech/project/fireflyalgorithm)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/FireflyAlgorithm.svg)](https://github.com/firefly-cpp/FireflyAlgorithm/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/FireflyAlgorithm.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/FireflyAlgorithm.svg)](http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/FireflyAlgorithm.svg)](http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm "Percentage of issues still open")
![GitHub contributors](https://img.shields.io/github/contributors/firefly-cpp/FireflyAlgorithm.svg)

## Installation:

```sh
pip install fireflyalgorithm
```
To install FireflyAlgorithm on Fedora, use:
```sh
dnf install python-fireflyalgorithm
```

## Usage:

```python
import numpy as np
from fireflyalgorithm import FireflyAlgorithm

def sphere(x):
    return np.sum(x ** 2)

FA = FireflyAlgorithm()
best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)
```

## Reference Papers:

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds.
Jozef Stefan Institute, Ljubljana, Slovenia, 2012

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.

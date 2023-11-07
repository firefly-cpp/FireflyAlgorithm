<p align="center">
  <img width="200" src="https://raw.githubusercontent.com/firefly-cpp/FireflyAlgorithm/master/.github/imgs/firefly_logo.png">
</p>

---

# Firefly Algorithm --- Implementation of Firefly algorithm in Python

---

[![PyPI Version](https://img.shields.io/pypi/v/fireflyalgorithm.svg)](https://pypi.python.org/pypi/fireflyalgorithm)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fireflyalgorithm.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fireflyalgorithm.svg)
[![Downloads](https://pepy.tech/badge/fireflyalgorithm)](https://pepy.tech/project/fireflyalgorithm)
[![AUR package](https://img.shields.io/aur/version/python-fireflyalgorithm?color=blue&label=Arch%20Linux&logo=arch-linux)](https://aur.archlinux.org/packages/python-fireflyalgorithm)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/FireflyAlgorithm.svg)](https://github.com/firefly-cpp/FireflyAlgorithm/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/FireflyAlgorithm.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/FireflyAlgorithm.svg)](http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/FireflyAlgorithm.svg)](http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm "Percentage of issues still open")
![GitHub contributors](https://img.shields.io/github/contributors/firefly-cpp/FireflyAlgorithm.svg)

## About

This package implements a nature-inspired algorithm for optimization called Firefly Algorithm (FA) in Python programming language.

## Installation:

Install FireflyAlgorithm with pip:
```sh
pip install fireflyalgorithm
```
To install FireflyAlgorithm on Fedora, use:
```sh
dnf install python-fireflyalgorithm
```
To install FireflyAlgorithm on Arch Linux, please use an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers):
```sh
$ yay -Syyu python-fireflyalgorithm
```

## Usage:

```python
from fireflyalgorithm import FireflyAlgorithm
from fireflyalgorithm.problems import sphere

FA = FireflyAlgorithm()
best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)
```

### Test functions

In the `fireflyalgorithm.problems` module, you can find the implementations of 33 popular optimization test problems.  Additionally, the module provides a utility function, `get_problem`, that allows you to retrieve a specific optimization problem function by providing its name as a string:

```python
from fireflyalgorithm.problems import get_problem

# same as from fireflyalgorithm.problems import rosenbrock
rosenbrock = get_problem('rosenbrock')
```

For more information about the implemented test functions, [click here](Problems.md)

### Command line interface

The package also comes with a simple command line interface which allows you to evaluate the algorithm on several
popular test functions

```shell
firefly-algorithm -h
```

```text
usage: firefly-algorithm [-h] --problem PROBLEM -d DIMENSION -l LOWER -u UPPER -nfes MAX_EVALS [-r RUNS] [--pop-size POP_SIZE] [--alpha ALPHA] [--beta-min BETA_MIN] [--gamma GAMMA] [--seed SEED]

Evaluate the Firefly Algorithm on one or more test functions

options:
  -h, --help            show this help message and exit
  --problem PROBLEM     Test problem to evaluate
  -d DIMENSION, --dimension DIMENSION
                        Dimension of the problem
  -l LOWER, --lower LOWER
                        Lower bounds of the problem
  -u UPPER, --upper UPPER
                        Upper bounds of the problem
  -nfes MAX_EVALS, --max-evals MAX_EVALS
                        Max number of fitness function evaluations
  -r RUNS, --runs RUNS  Number of runs of the algorithm
  --pop-size POP_SIZE   Population size
  --alpha ALPHA         Randomness strength
  --beta-min BETA_MIN   Attractiveness constant
  --gamma GAMMA         Absorption coefficient
  --seed SEED           Seed for the random number generator
```

**Note:** The CLI script can also run as a python module (python -m niaarm ...)


## Reference Papers:

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds.
Jozef Stefan Institute, Ljubljana, Slovenia, 2012

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.

## License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!

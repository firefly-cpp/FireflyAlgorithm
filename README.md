<p align="center">
  <img width="200" src="https://raw.githubusercontent.com/firefly-cpp/FireflyAlgorithm/master/.github/imgs/firefly_logo.png">
</p>

<h1 align="center">
Firefly Algorithm --- Implementation of Firefly algorithm in Python
</h1>

<p align="center">
  <img alt="PyPI Version" src="https://img.shields.io/pypi/v/fireflyalgorithm.svg" href="https://pypi.python.org/pypi/fireflyalgorithm">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fireflyalgorithm.svg">
  <img alt="Downloads" src="https://img.shields.io/pypi/dm/fireflyalgorithm.svg">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/firefly-cpp/FireflyAlgorithm">
  <img alt="AUR package" src="https://img.shields.io/aur/version/python-fireflyalgorithm?color=blue&label=Arch%20Linux&logo=arch-linux" href="https://aur.archlinux.org/packages/python-fireflyalgorithm">
  <img alt="GitHub license" src="https://img.shields.io/github/license/firefly-cpp/FireflyAlgorithm.svg" href="https://github.com/firefly-cpp/FireflyAlgorithm/blob/master/LICENSE">  
  <img alt="build" src="https://github.com/firefly-cpp/FireflyAlgorithm/actions/workflows/test.yml/badge.svg">
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/firefly-cpp/FireflyAlgorithm.svg">
  <img alt="Average time to resolve an issue" src="http://isitmaintained.com/badge/resolution/firefly-cpp/FireflyAlgorithm.svg" href="http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm">
  <img alt="Percentage of issues still open" src="http://isitmaintained.com/badge/open/firefly-cpp/FireflyAlgorithm.svg" href="http://isitmaintained.com/project/firefly-cpp/FireflyAlgorithm">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/firefly-cpp/FireflyAlgorithm.svg">
  <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/python:fireflyalgorithm.svg" href="https://repology.org/project/python:fireflyalgorithm/versions">
</p>

<p align="center">
  <img alt="DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.10430919.svg" href="https://doi.org/10.5281/zenodo.10430919">
</p>

<p align="center">
  <a href="#-about">📋 About</a> •
  <a href="#-installation">📦 Installation</a> •
  <a href="#-usage">🚀 Usage</a> •
  <a href="#-reference-papers">📚 Reference Papers</a> •
  <a href="#-cite-us">📄 Cite us</a> •
  <a href="#-license">🔑 License</a>
</p>

## 📋 About

This package implements a nature-inspired algorithm for optimization called Firefly Algorithm (FA) in Python programming language. 🌿🔍💻

## 📦 Installation

To install FireflyAlgorithm with pip, use:
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
To install FireflyAlgorithm on Alpine Linux, use:
```sh
$ apk add py3-fireflyalgorithm
```

## 🚀 Usage

```python
from fireflyalgorithm import FireflyAlgorithm
from fireflyalgorithm.problems import sphere

FA = FireflyAlgorithm()
best = FA.run(function=sphere, dim=10, lb=-5, ub=5, max_evals=10000)

print(best)
```

### Test functions 📈

In the `fireflyalgorithm.problems` module, you can find the implementations of 33 popular optimization test problems.  Additionally, the module provides a utility function, `get_problem`, that allows you to retrieve a specific optimization problem function by providing its name as a string:

```python
from fireflyalgorithm.problems import get_problem

# same as from fireflyalgorithm.problems import rosenbrock
rosenbrock = get_problem('rosenbrock')
```

For more information about the implemented test functions, [click here](Problems.md).

### Command line interface 🖥️

The package also comes with a simple command line interface which allows you to evaluate the algorithm on several popular test functions. 🔬

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

**Note:** The CLI script can also run as a python module (python -m fireflyalgorithm ...).


## 📚 Reference Papers

I. Fister Jr.,  X.-S. Yang,  I. Fister, J. Brest. [Memetic firefly algorithm for combinatorial optimization](http://www.iztok-jr-fister.eu/static/publications/44.pdf) in Bioinspired Optimization Methods and their Applications (BIOMA 2012), B. Filipic and J.Silc, Eds.
Jozef Stefan Institute, Ljubljana, Slovenia, 2012

I. Fister, I. Fister Jr.,  X.-S. Yang, J. Brest. [A comprehensive review of firefly algorithms](http://www.iztok-jr-fister.eu/static/publications/23.pdf). Swarm and Evolutionary Computation 13 (2013): 34-46.

## 📄 Cite us

Fister Jr., I., Pečnik, L., & Stupan, Ž. (2023). firefly-cpp/FireflyAlgorithm: 0.4.3 (0.4.3). Zenodo. [https://doi.org/10.5281/zenodo.10430919](https://doi.org/10.5281/zenodo.10430919)

## 🔑 License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!

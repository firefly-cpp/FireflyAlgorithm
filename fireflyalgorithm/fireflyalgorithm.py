import numpy as np
from numpy.random import default_rng


class FireflyAlgorithm():
    def __init__(self, function, dim, lb, ub, max_evals, pop_size=20, alpha=1.0, betamin=1.0, gamma=0.01, seed=None):
        self.function = function
        self.dim = dim
        self.lb = lb
        self.ub = ub
        self.max_evals = max_evals
        self.pop_size = pop_size
        self.alpha = alpha
        self.betamin = betamin
        self.gamma = gamma
        self.seed = seed

    def move(self):
        rng = default_rng(self.seed)
        fireflies = rng.uniform(self.lb, self.ub, (self.pop_size, self.dim))
        intensity = np.apply_along_axis(self.function, 1, fireflies)
        best = np.min(intensity)

        evaluations = self.pop_size
        new_alpha = self.alpha
        search_range = self.ub - self.lb

        while evaluations <= self.max_evals:
            new_alpha *= 0.97
            for i in range(self.pop_size):
                for j in range(self.pop_size):
                    if intensity[i] >= intensity[j]:
                        r = np.sum(np.square(fireflies[i] - fireflies[j]), axis=-1)
                        beta = self.betamin * np.exp(-self.gamma * r)
                        steps = new_alpha * (rng.random(self.dim) - 0.5) * search_range
                        fireflies[i] += beta * (fireflies[j] - fireflies[i]) + steps
                        fireflies[i] = np.clip(fireflies[i], self.lb, self.ub)
                        intensity[i] = self.function(fireflies[i])
                        evaluations += 1
                        best = min(intensity[i], best)
        return best

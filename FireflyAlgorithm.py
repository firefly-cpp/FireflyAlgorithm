import random
import math


class FireflyAlgorithm():

    def __init__(self, D, NP, nFES, alpha, betamin, gamma, LB, UB, function):
        self.D = D  # dimension of the problem
        self.NP = NP  # population size
        self.nFES = nFES  # number of function evaluations
        self.alpha = alpha  # alpha parameter
        self.betamin = betamin  # beta parameter
        self.gamma = gamma  # gamma parameter
        # sort of fireflies according to fitness value
        self.Index = [0] * self.NP
        self.Fireflies = [[0 for i in range(self.D)]
                          for j in range(self.NP)]  # firefly agents
        self.Fireflies_tmp = [[0 for i in range(self.D)] for j in range(
            self.NP)]  # intermediate pop
        self.Fitness = [0.0] * self.NP  # fitness values
        self.I = [0.0] * self.NP  # light intensity
        self.nbest = [0.0] * self.D  # the best solution found so far
        self.LB = LB  # lower bound
        self.UB = UB  # upper bound
        self.fbest = None  # the best
        self.evaluations = 0
        self.Fun = function

    def init_ffa(self):
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies[i][j] = random.uniform(
                    0, 1) * (self.UB - self.LB) + self.LB
            self.Fitness[i] = 1.0  # initialize attractiveness
            self.I[i] = self.Fitness[i]

    def alpha_new(self, a):
        delta = 1.0 - math.pow((math.pow(10.0, -4.0) / 0.9), 1.0 / float(a))
        return (1 - delta) * self.alpha

    def sort_ffa(self):
        self.Index = [i for i in range(self.NP)]
        self.I, self.Fitness, self.Index = [list(l) for l in zip(*sorted(zip(self.I, self.Fitness, self.Index)))]

    def replace_ffa(self):  # replace the old population according to the new Index values
        # copy original population to a temporary area
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies_tmp[i][j] = self.Fireflies[i][j]

        # generational selection in the sense of an EA
        for i in range(self.NP):
            for j in range(self.D):
                self.Fireflies[i][j] = self.Fireflies_tmp[self.Index[i]][j]

    def FindLimits(self, k):
        for i in range(self.D):
            if self.Fireflies[k][i] < self.LB:
                self.Fireflies[k][i] = self.LB
            if self.Fireflies[k][i] > self.UB:
                self.Fireflies[k][i] = self.UB

    def move_ffa(self):
        for i in range(self.NP):
            scale = abs(self.UB - self.LB)
            for j in range(self.NP):
                r = 0.0
                for k in range(self.D):
                    r += (self.Fireflies[i][k] - self.Fireflies[j][k]) * \
                        (self.Fireflies[i][k] - self.Fireflies[j][k])
                r = math.sqrt(r)
                if self.I[i] > self.I[j]:  # brighter and more attractive
                    beta0 = 1.0
                    beta = (beta0 - self.betamin) * \
                        math.exp(-self.gamma * math.pow(r, 2.0)) + self.betamin
                    for k in range(self.D):
                        r = random.uniform(0, 1)
                        tmpf = self.alpha * (r - 0.5) * scale
                        self.Fireflies[i][k] = self.Fireflies[i][
                            k] * (1.0 - beta) + self.Fireflies_tmp[j][k] * beta + tmpf
            self.FindLimits(i)

    def Run(self):
        self.init_ffa()
        
        while self.evaluations < self.nFES:

            # optional reducing of alpha
            self.alpha = self.alpha_new(self.nFES/self.NP)

            # evaluate new solutions
            for i in range(self.NP):
                self.Fitness[i] = self.Fun(self.D, self.Fireflies[i])
                self.evaluations = self.evaluations + 1
                self.I[i] = self.Fitness[i]

            # ranking fireflies by their light intensity
            self.sort_ffa()
            # replace old population
            self.replace_ffa()
            # find the current best
            self.fbest = self.I[0]
            # move all fireflies to the better locations
            self.move_ffa()
        
        return self.fbest

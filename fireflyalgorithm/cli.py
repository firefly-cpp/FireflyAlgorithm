import argparse
import numpy as np
from fireflyalgorithm.problems import PROBLEMS, get_problem
from fireflyalgorithm.fireflyalgorithm import FireflyAlgorithm


def get_parser():
    parser = argparse.ArgumentParser(
        prog="firefly-algorithm",
        description="Evaluate the Firefly Algorithm on one or more test functions",
    )

    problem_functions = list(PROBLEMS.keys())
    parser.add_argument(
        "--problem",
        type=str,
        required=True,
        choices=problem_functions,
        metavar="PROBLEM",
        help="Test problem to evaluate",
    )
    parser.add_argument(
        "-d", "--dimension", type=int, required=True, help="Dimension of the problem"
    )
    parser.add_argument(
        "-l", "--lower", type=float, required=True, help="Lower bounds of the problem"
    )
    parser.add_argument(
        "-u", "--upper", type=float, required=True, help="Upper bounds of the problem"
    )
    parser.add_argument(
        "-nfes",
        "--max-evals",
        type=int,
        required=True,
        help="Max number of fitness function evaluations",
    )
    parser.add_argument(
        "-r", "--runs", type=int, default=1, help="Number of runs of the algorithm"
    )
    parser.add_argument("--pop-size", type=int, default=20, help="Population size")
    parser.add_argument("--alpha", type=float, default=1.0, help="Randomness strength")
    parser.add_argument(
        "--beta-min", type=float, default=1.0, help="Attractiveness constant"
    )
    parser.add_argument(
        "--gamma", type=float, default=0.01, help="Absorption coefficient"
    )
    parser.add_argument("--seed", type=int, help="Seed for the random number generator")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    algorithm = FireflyAlgorithm(
        args.pop_size, args.alpha, args.beta_min, args.gamma, args.seed
    )
    problem = get_problem(args.problem)
    dim = args.dimension
    lb = args.lower
    ub = args.upper
    max_evals = args.max_evals
    runs = args.runs

    fitness = np.empty(runs)
    for i in range(runs):
        fitness[i] = algorithm.run(problem, dim, lb, ub, max_evals)

    if runs == 1:
        print(f"Best fitness: {fitness[0]}")
    else:
        print(f"Best: {fitness.min()}")
        print(f"Worst: {fitness.max()}")
        print(f"Mean: {fitness.mean()}")
        print(f"Std: {fitness.std()}")

    return 0

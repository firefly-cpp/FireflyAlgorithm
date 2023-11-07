import numpy as np


def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    dim = len(x)

    val1 = np.sum(np.square(x))
    val2 = np.sum(np.cos(c * x))

    temp1 = -b * np.sqrt(val1 / dim)
    temp2 = val2 / dim

    return -a * np.exp(temp1) - np.exp(temp2) + a + np.exp(1)


def alpine1(x):
    return np.sum(np.abs(np.sin(x) + 0.1 * x))


def alpine2(x):
    return np.prod(np.sqrt(x) * np.sin(x))


def cigar(x):
    return x[0] ** 2 + 1000000 * np.sum(x[1:] ** 2)


def cosine_mixture(x):
    return -0.1 * np.sum(np.cos(5 * np.pi * x)) - np.sum(x**2)


def csendes(x):
    mask = x != 0
    return np.sum(np.power(x[mask], 6) * (2 + np.sin(1 / x[mask])))


def dixon_price(x):
    dim = len(x)
    indices = np.arange(2, dim)
    val = np.sum(indices * (2 * x[2:] ** 2 - x[1 : dim - 1]) ** 2)
    return (x[0] - 1) ** 2 + val


def griewank(x):
    dim = len(x)
    i = np.arange(1, dim + 1)
    val1 = np.sum(x**2 / 4000)
    val2 = np.prod(np.cos(x / np.sqrt(i)))
    return val1 - val2 + 1


def katsuura(x):
    dim = len(x)
    k = np.atleast_2d(np.arange(1, 33)).T
    i = np.arange(1, dim + 1)
    inner = np.round(2**k * x) * (2.0 ** (-k))
    return np.prod(np.sum(inner, axis=0) * i + 1)


def levy(x):
    w = 1 + (x - 1) / 4
    wi = w[:-1]
    term1 = np.sin(np.pi * w[0]) ** 2
    term2 = np.sum((wi - 1) ** 2 * (1 + 10 * np.sin(np.pi * wi + 1)))
    term3 = (w[-1] - 1) ** 2 * (1 + np.sin(2 * np.pi * w[-1]) ** 2)
    return term1 + term2 + term3


def michalewicz(x):
    dim = len(x)
    m = 10
    i = np.arange(1, dim + 1)
    return -np.sum(np.sin(x) * np.sin(i * x**2 / np.pi) ** (2 * m))


def perm1(x):
    dim = len(x)
    beta = 0.5
    k = np.atleast_2d(np.arange(dim) + 1).T
    j = np.atleast_2d(np.arange(dim) + 1)
    s = (j**k + beta) * ((x / j) ** k - 1)
    return np.sum(np.sum(s, axis=1) ** 2)


def perm2(x):
    dim = len(x)
    beta = 10
    k = np.atleast_2d(np.arange(dim) + 1).T
    j = np.atleast_2d(np.arange(dim) + 1)
    s = (j + beta) * (x**k - (1 / j) ** k)
    return np.sum(np.sum(s, axis=1) ** 2)


def pinter(x):
    dim = len(x)
    x = np.asarray(x)
    sub = np.roll(x, 1)
    add = np.roll(x, -1)
    indices = np.arange(1, dim + 1)

    a = sub * np.sin(x) + np.sin(add)
    b = (sub * sub) - 2 * x + 3 * add - np.cos(x) + 1

    val1 = np.sum(indices * x * x)
    val2 = np.sum(20 * indices * np.power(np.sin(a), 2))
    val3 = np.sum(indices * np.log10(1 + indices * np.power(b, 2)))

    return val1 + val2 + val3


def powell(x):
    x1 = x[0::4]
    x2 = x[1::4]
    x3 = x[2::4]
    x4 = x[3::4]

    term1 = (x1 + 10 * x2) ** 2
    term2 = 5 * (x3 - x4) ** 2
    term3 = (x2 - 2 * x3) ** 4
    term4 = 10 * (x1 - x4) ** 4
    return np.sum(term1 + term2 + term3 + term4)


def qing(x):
    dim = len(x)
    return np.sum(np.power(x**2 - np.arange(1, dim + 1), 2))


def quintic(x):
    return np.sum(np.abs(x**5 - 3 * x**4 + 4 * x**3 + 2 * x**2 - 10 * x - 4))


def rastrigin(x):
    dim = len(x)
    return 10 * dim + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


def rosenbrock(x):
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2, axis=0)


def salomon(x):
    val = np.sqrt(np.sum(x**2))
    return 1 - np.cos(2 * np.pi * val) + 0.1 * val


def schaffer2(x):
    return (
        0.5
        + (np.sin(x[0] ** 2 - x[1] ** 2) ** 2 - 0.5)
        / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2
    )


def schaffer4(x):
    return (
        0.5
        + (np.cos(np.sin(abs(x[0] ** 2 - x[1] ** 2))) ** 2 - 0.5)
        / (1 + 0.001 * (x[0] ** 2 + x[1] ** 2)) ** 2
    )


def schwefel(x):
    dim = len(x)
    return 418.982887272433799807913601398 * dim - np.sum(
        x * np.sin(np.sqrt(np.abs(x)))
    )


def schwefel221(x):
    return np.amax(np.abs(x))


def schwefel222(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))


def sphere(x):
    return np.sum(x**2)


def step(x):
    return np.sum(np.floor(np.abs(x)))


def step2(x):
    return np.sum(np.floor(x + 0.5) ** 2)


def styblinski_tang(x):
    return 0.5 * np.sum(x**4 - 16 * x**2 + 5 * x)


def trid(x):
    sum1 = np.sum((x - 1) ** 2)
    sum2 = np.sum(x[1:] * x[:-1])
    return sum1 - sum2


def weierstrass(x):
    dim = len(x)
    kmax = 20
    a = 0.5
    b = 3

    k = np.atleast_2d(np.arange(kmax + 1)).T
    t1 = a**k * np.cos(2 * np.pi * b**k * (x + 0.5))
    t2 = dim * np.sum(a**k.T * np.cos(np.pi * b**k.T))

    return np.sum(np.sum(t1, axis=0)) - t2


def whitley(x):
    xi = x
    xj = np.atleast_2d(x).T

    temp = 100 * ((xi**2) - xj) + (1 - xj) ** 2
    inner = (temp**2 / 4000) - np.cos(temp) + 1
    return np.sum(np.sum(inner, axis=0))


def zakharov(x):
    dim = len(x)
    sum1 = np.sum(x**2)
    sum2 = 0.5 * np.sum(np.arange(1, dim + 1) * x)
    return sum1 + sum2**2 + sum2**4


PROBLEMS = {
    "ackley": ackley,
    "alpine1": alpine1,
    "alpine2": alpine2,
    "cigar": cigar,
    "cosine_mixture": cosine_mixture,
    "csendes": csendes,
    "dixon_price": dixon_price,
    "griewank": griewank,
    "katsuura": katsuura,
    "levy": levy,
    "michalewicz": michalewicz,
    "perm1": perm1,
    "perm2": perm2,
    "pinter": pinter,
    "powell": powell,
    "qing": qing,
    "quintic": quintic,
    "rastrigin": rastrigin,
    "rosenbrock": rosenbrock,
    "salomon": salomon,
    "schaffer2": schaffer2,
    "schaffer4": schaffer4,
    "schwefel": schwefel,
    "schwefel221": schwefel221,
    "schwefel222": schwefel222,
    "sphere": sphere,
    "step": step,
    "step2": step2,
    "styblinski_tang": styblinski_tang,
    "trid": trid,
    "weierstrass": weierstrass,
    "whitley": whitley,
    "zakharov": zakharov,
}


def get_problem(name):
    return PROBLEMS[name]

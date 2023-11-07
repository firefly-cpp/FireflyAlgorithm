from unittest import TestCase
import numpy as np
from fireflyalgorithm.problems import (
    get_problem,
    ackley,
    alpine1,
    alpine2,
    cigar,
    cosine_mixture,
    csendes,
    dixon_price,
    griewank,
    katsuura,
    levy,
    michalewicz,
    perm1,
    perm2,
    pinter,
    powell,
    qing,
    quintic,
    rastrigin,
    rosenbrock,
    salomon,
    schaffer2,
    schaffer4,
    schwefel,
    schwefel221,
    schwefel222,
    sphere,
    step,
    step2,
    styblinski_tang,
    trid,
    weierstrass,
    whitley,
    zakharov,
)


class TestProblems(TestCase):
    def test_problem_factory(self):
        self.assertRaises(KeyError, get_problem, "spherekjl2")
        self.assertEqual(get_problem("ackley"), ackley)
        self.assertEqual(get_problem("alpine1"), alpine1)
        self.assertEqual(get_problem("alpine2"), alpine2)
        self.assertEqual(get_problem("cigar"), cigar)
        self.assertEqual(get_problem("cosine_mixture"), cosine_mixture)
        self.assertEqual(get_problem("csendes"), csendes)
        self.assertEqual(get_problem("dixon_price"), dixon_price)
        self.assertEqual(get_problem("griewank"), griewank)
        self.assertEqual(get_problem("katsuura"), katsuura)
        self.assertEqual(get_problem("levy"), levy)
        self.assertEqual(get_problem("michalewicz"), michalewicz)
        self.assertEqual(get_problem("perm1"), perm1)
        self.assertEqual(get_problem("perm2"), perm2)
        self.assertEqual(get_problem("pinter"), pinter)
        self.assertEqual(get_problem("powell"), powell)
        self.assertEqual(get_problem("qing"), qing)
        self.assertEqual(get_problem("quintic"), quintic)
        self.assertEqual(get_problem("rastrigin"), rastrigin)
        self.assertEqual(get_problem("rosenbrock"), rosenbrock)
        self.assertEqual(get_problem("salomon"), salomon)
        self.assertEqual(get_problem("schaffer2"), schaffer2)
        self.assertEqual(get_problem("schaffer4"), schaffer4)
        self.assertEqual(get_problem("schwefel"), schwefel)
        self.assertEqual(get_problem("schwefel221"), schwefel221)
        self.assertEqual(get_problem("schwefel222"), schwefel222)
        self.assertEqual(get_problem("sphere"), sphere)
        self.assertEqual(get_problem("step"), step)
        self.assertEqual(get_problem("step2"), step2)
        self.assertEqual(get_problem("styblinski_tang"), styblinski_tang)
        self.assertEqual(get_problem("trid"), trid)
        self.assertEqual(get_problem("weierstrass"), weierstrass)
        self.assertEqual(get_problem("whitley"), whitley)
        self.assertEqual(get_problem("zakharov"), zakharov)

    def test_ackley(self):
        x = np.zeros(5)
        self.assertAlmostEqual(ackley(x), 0.0)

    def test_alpine1(self):
        x = np.zeros(5)
        self.assertAlmostEqual(alpine1(x), 0.0)

    def test_alpine2(self):
        x = np.full(5, 7.9170526982459462172)
        self.assertAlmostEqual(alpine2(x), 2.8081311800070053291**5)

    def test_cigar(self):
        x = np.zeros(5)
        self.assertAlmostEqual(cigar(x), 0.0)

    def test_cosine_mixture(self):
        x = np.zeros(5)
        self.assertAlmostEqual(cosine_mixture(x), -0.5)

    def test_csendes(self):
        x = np.zeros(5)
        self.assertAlmostEqual(csendes(x), 0.0)

    def test_dixon_price(self):
        x = np.array([2 ** -((2**i - 2) / 2**i) for i in range(1, 6)])
        self.assertAlmostEqual(dixon_price(x), 0.0)

    def test_griewank(self):
        x = np.zeros(5)
        self.assertAlmostEqual(griewank(x), 0.0)

    def test_katsuura(self):
        x = np.zeros(5)
        self.assertAlmostEqual(katsuura(x), 1.0)

    def test_levy(self):
        x = np.full(5, 1)
        self.assertAlmostEqual(levy(x), 0.0)

    def test_michalewicz(self):
        x = np.array([2.20290552014618, 1.57079632677565])
        self.assertAlmostEqual(michalewicz(x), -1.80130341009855321)

    def test_perm1(self):
        x = np.arange(1, 6)
        self.assertAlmostEqual(perm1(x), 0.0)

    def test_perm2(self):
        x = 1 / np.arange(1, 6)
        self.assertAlmostEqual(perm2(x), 0.0)

    def test_pinter(self):
        x = np.zeros(5)
        self.assertAlmostEqual(pinter(x), 0.0)

    def test_powell(self):
        x = np.zeros(5)
        self.assertAlmostEqual(powell(x), 0.0)

    def test_qing(self):
        x = np.sqrt(np.arange(1, 6))
        self.assertAlmostEqual(qing(x), 0.0)

    def test_quintic(self):
        x = np.full(5, -1)
        self.assertAlmostEqual(quintic(x), 0.0)

    def test_rastrigin(self):
        x = np.zeros(5)
        self.assertAlmostEqual(rastrigin(x), 0.0)

    def test_rosenbrock(self):
        x = np.full(5, 1)
        self.assertAlmostEqual(rosenbrock(x), 0.0)

    def test_salomon(self):
        x = np.zeros(5)
        self.assertAlmostEqual(rastrigin(x), 0.0)

    def test_schaffer2(self):
        x = np.zeros(5)
        self.assertAlmostEqual(schaffer2(x), 0.0)

    def test_schaffer4(self):
        x1 = np.array([0, 1.253131828792882])
        x2 = np.array([0, -1.253131828792882])
        x3 = np.array([1.253131828792882, 0])
        x4 = np.array([-1.253131828792882, 0])
        self.assertAlmostEqual(schaffer4(x1), 0.292578632035980)
        self.assertAlmostEqual(schaffer4(x2), 0.292578632035980)
        self.assertAlmostEqual(schaffer4(x3), 0.292578632035980)
        self.assertAlmostEqual(schaffer4(x4), 0.292578632035980)

    def test_schwefel(self):
        x = np.full(5, 420.968746)
        self.assertAlmostEqual(schwefel(x), 0.0)

    def test_schwefel21(self):
        x = np.zeros(5)
        self.assertAlmostEqual(schwefel221(x), 0.0)

    def test_schwefel22(self):
        x = np.zeros(5)
        self.assertAlmostEqual(schwefel222(x), 0.0)

    def test_sphere(self):
        x = np.zeros(5)
        self.assertAlmostEqual(sphere(x), 0.0)

    def test_step(self):
        x = np.full(5, 0.5)
        self.assertAlmostEqual(step(x), 0.0)

    def test_step2(self):
        x = np.full(5, -0.5)
        self.assertAlmostEqual(step2(x), 0.0)

    def test_styblinski_tang(self):
        x = np.full(5, -2.903534018185960)
        self.assertAlmostEqual(styblinski_tang(x), -39.16616570377142 * 5)

    def test_trid(self):
        x = np.array([6, 10, 12, 12, 10, 6])
        self.assertAlmostEqual(trid(x), -50)

    def test_weierstrass(self):
        x = np.zeros(5)
        self.assertAlmostEqual(weierstrass(x), 0.0)

    def test_whitley(self):
        x = np.full(5, 1)
        self.assertAlmostEqual(whitley(x), 0.0)

    def test_zakharov(self):
        x = np.zeros(5)
        self.assertAlmostEqual(zakharov(x), 0.0)

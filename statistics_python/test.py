import unittest

from stats import mean_value
import probability
from discrete_distributions import Binomial, Geometric, NegBinomial, Poisson

class TestStats(unittest.TestCase):
    def test_meanValue(self):
        print("")
        print("\ntesting mean value function")
        self.assertEqual(mean_value([1,2,3,4,5]),3)
        self.assertEqual(mean_value(1),1)
        self.assertRaises(ValueError, mean_value,)

class TestProb(unittest.TestCase):

    def test_factorial(self):
        print("\nTesting factorial...")
        self.assertEqual(probability.factorial(1),1)
    def test_permutation(self):
        print("\nTesting permutation...")
        self.assertEqual(probability.permutation(5,3),60)
    def test_combination(self):
        print("\nTesting combination...")
        self.assertEqual(probability.combination(5,3),10)

class TestBinomial(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.binomial = Binomial(5,0.1)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_binomialDistribution(self):
        print("\nTesting binomial distribution unit test...")
        self.assertEqual(self.binomial.Distribution(5), 1.0)
    def test_binomialMassProbability(self):
        print("\nTesting binomial probability unit test...")
        self.assertEqual(self.binomial.MassProbability(0), 0.5904900000000001)
    def test_binomialProbability(self):
        print("\nTesting binomial probability unit test...")
        self.assertEqual(self.binomial.Probability(1,3), 0.40905)

class TestGeometric(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.geometric = Geometric(0.1)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_geometricDistribution(self):
        print("\nTesting geometric distribution unit test...")
        self.assertEqual(self.geometric.Distribution(1), 0.1)
    def test_geometricMassProbability(self):
        print("\nTesting geometric mass probability unit test...")
        self.assertEqual(self.geometric.MassProbability(1), 0.1)
    def test_geometricProbability(self):
        print("\nTesting geometric probability within an interval unit test...")
        self.assertEqual(self.geometric.Probability(1,2), 0.19)

class TestNegBinomial(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.negBinomial = NegBinomial(1, 0.1)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_negBinomialDistribution(self):
        print("\nTesting negative binomial distribution unit test...")
        self.assertEqual(self.negBinomial.Distribution(1), 0.1)
    def test_negBinomialMassProbability(self):
        print("\nTesting negative binomial mass probability unit test...")
        self.assertEqual(self.negBinomial.MassProbability(1), 0.1)
    def test_negBinomialProbability(self):
        print("\nTesting negative binomial probability within an interval unit test...")
        self.assertEqual(self.negBinomial.Probability(1,2), 0.19)
class TestPoisson(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.poisson = Poisson(2)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_poissonDistribution(self):
        print("\nTesting poisson distribution unit test...")
        self.assertEqual(self.poisson.Distribution(1), 0.40600585070426376)
    def test_poissonMassProbability(self):
        print("\nTesting poisson mass probability unit test...")
        self.assertEqual(self.poisson.MassProbability(1), 0.2706705671361758)
    def test_poissonProbability(self):
        print("\nTesting poisson probability within an interval unit test...")
        self.assertEqual(self.poisson.Probability(1,2), 0.5413411342723518)

if __name__ == '__main__':
    unittest.main()
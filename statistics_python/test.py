import unittest

from stats import mean_value
import probability
from Binomial import Binomial

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
    def test_binomialProbability(self):
        print("\nTesting binomial probability unit test...")
        self.assertEqual(self.binomial.MassProbability(0), 0.5904900000000001)

if __name__ == '__main__':
    unittest.main()
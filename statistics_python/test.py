import unittest
import sys
sys.dont_write_bytecode = True

from stats import mean_value
from combinatory import *
from discrete_distributions import *
from continuous_distributions import *
from mathematics import PI, sqrt, factorial, gamma

class TestStats(unittest.TestCase):
    def test_meanValue(self):
        print("")
        print("\ntesting mean value function")
        self.assertEqual(mean_value([1,2,3,4,5]),3)
        self.assertEqual(mean_value(1),1)
        self.assertRaises(ValueError, mean_value,)

class TestProb(unittest.TestCase):

    def test_permutation(self):
        print("\nTesting permutation...")
        self.assertEqual(permutation(5,3),60)
    def test_combination(self):
        print("\nTesting combination...")
        self.assertEqual(combination(5,3),10)

class TestMath(unittest.TestCase):

    def test_factorial(self):
        print("\nTesting factorial...")
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(3),6)
    def test_gamma(self):
        print("\nTesting Gamma...")
        self.assertEqual(gamma(1/2), sqrt(PI))
        self.assertEqual(gamma(3/2),0.5*sqrt(PI))
        self.assertEqual(gamma(5/2),(3/4)*sqrt(PI))

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
        self.assertEqual(self.poisson.Distribution(1), 0.4060058497086582)
    def test_poissonMassProbability(self):
        print("\nTesting poisson mass probability unit test...")
        self.assertEqual(self.poisson.MassProbability(1), 0.2706705664724388)
    def test_poissonProbability(self):
        print("\nTesting poisson probability within an interval unit test...")
        self.assertEqual(self.poisson.Probability(1,2), 0.5413411329448776)

class TestNormal(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.normal = Normal(0,1.0)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_normalDistribution(self):
        print("\nTesting normal distribution unit test...")
        self.assertEqual(self.normal.Distribution(0), 0.5)
    def test_normalDensity(self):
        print("\nTesting poisson mass probability unit test...")
        self.assertEqual(self.normal.Density(1), 0.24197072451894752)
    def test_normalProbability(self):
        print("\nTesting poisson probability within an interval unit test...")
        self.assertEqual(self.normal.Probability(-1.96,1.96), 0.950004209703631)

class TestExponential(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.exponential = Exponential(2.0)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_exponentialDistribution(self):
        print("\nTesting exponential distribution unit test...")
        self.assertEqual(self.exponential.Distribution(2.0), 0.632120558827838)
    def test_exponentialDensity(self):
        print("\nTesting exponential density unit test...")
        self.assertEqual(self.exponential.Density(0), 0.5)
    def test_exponentialProbability(self):
        print("\nTesting exponential probability within an interval unit test...")
        self.assertEqual(self.exponential.Probability(0.0,2.0), 0.632120558827838)

class TestUniform(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.uniform = Uniform(0.0, 4.0)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_uniformDistribution(self):
        print("\nTesting uniform distribution unit test...")
        self.assertEqual(self.uniform.Distribution(2.0), 0.5)
    def test_uniformDensity(self):
        print("\nTesting uniform density unit test...")
        self.assertEqual(self.uniform.Density(3), 0.25)
    def test_uniformProbability(self):
        print("\nTesting uniform probability within an interval unit test...")
        self.assertEqual(self.uniform.Probability(1.0,2.0),0.25 )

if __name__ == '__main__':
    unittest.main()
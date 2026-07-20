import unittest
import sys
sys.dont_write_bytecode = True

from stats import mean_value
from combinatory import *
from discrete_distributions import *
from continuous_distributions import *
from mathematics import PI, sqrt, factorial, gamma, sine, cosine, dotProduct
from iterative_methods import GauusSeidel_Method, Jacobi_Method
from matrix import Matrix

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
    def test_sine(self):
        print("\nTesting sine function...")
        self.assertAlmostEqual(sine(PI/2,tol=10**-20, n_sum=1000),1.0,delta=3*10**-16)
    def test_cosine(self):
        print("\nTesting cosine function...")
        self.assertAlmostEqual(cosine(PI/2,tol=10**-20, n_sum=1000),0.0,delta=3*10**-16)
    def test_dotProduct(self):
        print("\nTesting dot product...")
        self.assertEqual(dotProduct([1,1,1,1],[1,2,3,4]),10)

class TestIterativeMethods(unittest.TestCase):

    def test_GaussSeidel(self):
        print("\nTest Gauss Seidel Method...")
        A_1=[[12,3,-5], [1,5,3], [3,7,13]]
        b_1=[1,28,76]
        self.assertEqual(GauusSeidel_Method(A=A_1,b=b_1, x_initial=[1,0,1], n_max_iter=10)[0],[1.0000022061063778, 2.9999988404211484, 4.000000115287141])

    def test_Jacobi(self):
        print("\nTest Jacobi method...")
        A_1=[[12,3,-5], [1,5,3], [3,7,13]]
        b_1=[1,28,76]
        self.assertEqual(Jacobi_Method(A=A_1,b=b_1, x_initial=[1,0,1], n_max_iter=30)[0],[1.0000000431288647, 2.999999753685029, 3.9999997092977795])

class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.A=Matrix(3,2)
        self.A[0]=[3,2]
        self.A[1]=[4,5]
        self.B=Matrix(3,2)
        self.B[2]=[1,1]
        self.D=Matrix(2,3, init_value=1)
        return super().setUp()
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
    def tearDown(self):
        return super().tearDown()
    def test_MatrixAdd(self):
        print("\nTesting Matrix addition...")
        self.assertEqual((self.A+self.B).Matrix, [[3, 2], [4, 5], [1, 1]])
    def test_MatrixMult(self):
        print("\nTesting Matrix multiplication...")
        self.assertEqual((self.D*self.A).Matrix, [[7, 7], [7, 7]])
    def test_MatrixTranspose(self):
        print("\nTesting Matrix transpose...")
        self.assertEqual((self.A.transpose()).Matrix, [[3, 4, 0], [2, 5, 0]])
    def test_ScalarMult(self):
        print("\nTesting Matrix Scalar multiplication...")
        self.assertEqual((3*self.A).Matrix, [[9, 6], [12, 15], [0, 0]])
    def test_NegativeMatrix(self):
        print("\nTesting Negative matrix...")
        self.assertEqual((-self.A).Matrix, [[-3, -2], [-4, -5], [0, 0]])
    def test_PowerMatrix(self):
        print("\nTesting Power matrix...")
        self.A=Matrix(rows=4,columns=4,init_value=5.0)
        self.assertEqual((self.A**3).Matrix,[[2000.0, 2000.0, 2000.0, 2000.0], [2000.0, 2000.0, 2000.0, 2000.0], [2000.0, 2000.0, 2000.0, 2000.0], [2000.0, 2000.0, 2000.0, 2000.0]])

    def test_NormsMatrix(self):
        print("\nTesting Matrix norms ...")
        self.B=Matrix(3,3)
        self.B[0]=[3,6,-1]
        self.B[1]=[3,1,0]
        self.B[2]=[2,4,7]
        self.assertEqual((self.B.norm_1(),self.B.norm_infinity()),(11,13))
    
    def test_InverseMatrix(self):
        print("\nTesting Inverse of a Matrix...")
        self.I=Matrix(4,4).identity()
        self.A=Matrix(4,4)
        self.A[0]=[0,7,-5,3]
        self.A[1]=[2,8,0,4]
        self.A[2]=[3,12,0,5]
        self.A[3]=[1,3,1,3]
        self.A_inv=self.A.inverse()
        self.assertAlmostEqual((self.A*self.A_inv).norm_1(),self.I.norm_1(),delta = 10)

class TestBinomial(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()
    def setUp(self):
        self.binomial = Binomial(prob=0.1,n_trials=5)
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
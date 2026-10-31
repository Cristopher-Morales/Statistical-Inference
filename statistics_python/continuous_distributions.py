"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing classes for continuous distributions commonly used in statistics, probability, machine learning and others.

"""

from mathematics import SQRT_PI, SQRT_2, exp, sqrt, erf, gamma, checkInteger, Newton_Raphson, ln


class Uniform():

    r"""Class for defining the Probability Density Function (PDF) of the Uniform distribution.

    Parameters
    ----------
    a : float
        Lower-Limit uniform distribution. 
    b : float
        Upper-Limit uniform distribution.

    Note
    ----

    parameter b must be bigger than a. In case, b<a, they are swapped internally (a,b=b,a).
    """

    def __init__(self, a, b):
        if (isinstance(a, str) or isinstance(b, str)):
            raise TypeError(str(a)+","+str(b) +
                            " must be real number, and "+str(a)+"<"+str(b))
        if (b == a):
            raise ValueError(str(a)+" and "+str(b)+" must be different for defining a "
                             "well-defined uniform distribution")
        elif (b < a):
            # swap values
            a, b = b, a
        self.a = a
        self.b = b
        self.expectedValue = (a+b)/2
        self.variance = (b-a)**2/12

    def Density(self, x) -> float:
        r"""Method for computing Probability Density Function (PDF) of the Uniform distribution.
        
        f(x) = 1 / (b - a),  if a <= x <= b
        
                0,            otherwise
        
        Parameters
        ----------
        x : float
            Point where the probability density function is evaluated.
        
        Returns
        ------
        float
            Probability density evaluated at x. Returns 1 / (b - a) if x
            belongs to the interval [a, b], and 0 otherwise.

        Note
        ----

        The continuous uniform distribution is defined by two parameters:
        a (lower bound) and b (upper bound), where a < b.

        The probability density is constant over the interval [a, b]
        and zero outside this interval.
        """
        if (x <= self.a or x >= self.b):
            return 0
        else:
            return 1.0/(self.b-self.a)

    def Distribution(self, x) -> float:
        r"""Compute the Cumulative Distribution Function(CDF) of the continuous Uniform distribution.

        $$F(x) =
        \\begin{cases}
            0, & x < a, \\\\
            \\dfrac{x-a}{b-a}, & a \\leq x \\leq b, \\\\
            1, & x > b.
        \\end{cases}$$
        
        Parameters
        ----------
        x : float
            Point where the Cumulative Distribution Function is evaluated.

        Returns
        --------
        float
            Cumulative probability up to x, i.e. P(X<=x).

        Note
        ----

        CDF returns:
        -0 if x is smaller than lower bound of the uniform distribution.
        -1 if x is bigger than upper bound of the uniform distribution.
        - (x-a)/(b-a) is x belong to the interval [a,b].
        """
        
        if x < self.a:
            return 0
        elif self.a <= x or x < self.b:
            return (x-self.a)/(self.b-self.a)
        else:
            return 1

    def Probability(self, x, y) -> float:
        if x > y:
            raise ValueError(str(x)+" must be smaller than " + str(y))
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        assert 0 < z < 1, f'{z} must be a valid probability between 0 and 1'
        return z*(self.b-self.a)+self.a


class Exponential():

    def __init__(self, param_lambda):
        if (isinstance(param_lambda, str)):
            raise TypeError(str(param_lambda)+" must be real number")
        self.param_lambda = param_lambda
        self.expectedValue = param_lambda
        self.variance = param_lambda**2

    def Density(self, x):
        if (x < 0):
            return 0
        else:
            return 1.0/self.param_lambda * exp(-x/self.param_lambda)

    def Distribution(self, x):
        if x < 0:
            return 0
        else:
            return 1.0 - exp(-x/self.param_lambda)

    def Probability(self, x, y):
        if x > y:
            raise ValueError(str(x)+" must be smaller than " + str(y))
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        assert 0 < z < 1, f'{z} must be a valid probability between 0 and 1'
        return -1.0*self.param_lambda*ln(1.0-z)


class Normal():

    def __init__(self, mean=None, variance=None):
        if (variance != None and variance < 0):
            raise ValueError("Variance "+str(variance) +
                             " must be a positive value.")
        if (mean is None or variance is None):
            mean = 0.0
            variance = 1.0
            print(
                f'Normal standard distribution is assumed (mean = {mean} and variance = {variance})')
        self.mean = mean
        self.standardDeviation = sqrt(variance)
        self.expectedValue = mean
        self.variance = variance
        self.normalFactor = 1.0/(SQRT_2*SQRT_PI*self.standardDeviation)

    def Density(self, x):
        return self.normalFactor * exp(-0.5*((x-self.mean)/self.standardDeviation)**2)

    def Distribution(self, x):
        normalized_x = (x-self.mean)/(SQRT_2*self.standardDeviation)
        if x >= 0:
            return 0.5*(1 + erf(normalized_x))
        else:
            return 0.5*(1 - erf(-1.0*normalized_x))

    def Probability(self, x, y):
        if x > y:
            raise ValueError(str(x)+" must be smaller than " + str(y))
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        assert 0 < z < 1, f'{z} must be a valid probability between 0 and 1'
        return Newton_Raphson(lambda x: self.Distribution(x)-z, lambda x: self.Density(x), x_0=self.mean)


class Gamma():

    r"""Class for defining the Probability Density Function (PDF) of the Gamma distribution.

    This implementation uses the **shape-scale** parameterization.

    Parameters
    ----------
    alpha : float
        The shape parameter (often denoted as 'k' or 'alpha'). Must be > 0.
    beta : float
        The scale parameter (inverse rate, often denoted as 'beta'). Must be > 0.

    Note
    ----

    If you are looking for the shape-rate parameterization (where rate = 1/scale),
    pass `1 / rate` as the `beta` argument.
    """

    def __init__(self, alpha: float, beta: float | None = None):
        if (alpha is None or checkInteger(alpha)):
            raise ValueError(
                "alpha parameter must be an positive integer or half-integer")
        else:
            self.alpha = alpha
        if (beta is None):
            print("\n beta value is initialized to 1.0")
            self.beta = 1.0
        elif (beta < 0):
            raise ValueError("scale parameter beta must be bigger than zero")
        else:
            self.beta = beta
        self.expectedValue = self.alpha*self.beta
        self.variance = self.expectedValue*self.beta
        self._gammaFactor = 1/((self.beta**self.alpha)*gamma(self.alpha))

    def Density(self, x):
        r"""
        Function for computing the **PDF** of the Gamma Distribution.

        Parameters
        ----------
        x : float
            Value where the PDF is going to be evaluated. If x<0, then it returns 0.
            otherwise, it returns the PDF evaluated in that value.
        """
        if x < 0:
            return 0
        return self._gammaFactor * exp(-x/self.beta)*x**(self.alpha-1.0)


class chiSquared(Gamma):
    r"""Class for defining the Probability Density Function (PDF) of the chiSquared distribution.

    Parameters
    ----------
    n : int
        degrees of freedom. Must be >0.
    """

    def __init__(self, n):
        if (isinstance(n, int) == False or n <= 0):
            raise ValueError(str(n)+" must be an integer bigger than zero")
        super().__init__(n/2, 2.0)

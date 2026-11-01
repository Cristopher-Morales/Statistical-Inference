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
            raise TypeError(f'{a},{b} must be real number, and {a} < {b}')
        if (b == a):
            raise ValueError(
                f'{a} and {b} must be different for defining a well-defined uniform distribution')
        elif (b < a):
            # swap values
            a, b = b, a
        self.a = a
        self.b = b
        self.expectedValue = (a+b)/2
        self.variance = (b-a)**2/12

    def Density(self, x) -> float:
        r"""Method for computing Probability Density Function (PDF) of the Uniform distribution.
        
        $$f(x) = \left\lbrace\begin{array}{cc}1 / (b - a)&\;  \mathrm{if}\; a <= x <= b,\\ 0,&\ \mathrm{otherwise}\end{array}\right.$$
        
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

        $$F(x) =\left\lbrace\begin{array}{cc}0,& & x < a, \\ \dfrac{x-a}{b-a}, & a \leq x \leq b, \\1, & x > b.\end{array}\right.$$
        
        
        
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
        r"""Compute the Probability of the continuous Uniform distribution.

        Parameters
        ----------
        x : float
            Lower bound of the interval where the probability is computed.
        y : float
            Upper bound of the interval where the probability is computed.

        Returns
        --------
        float
            Probability of X belongs to intervals [x,y], i.e. P(x<=X<=y).

        """
        if x > y:
            raise ValueError(f'{x} must be smaller than {y}')
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        r"""Compute the inverse of the continuous Uniform distribution.
        
        Parameters
        ----------
        z : float
            Cumulative probability of the uniform distribution, i.e., P(X<=x)=z

        Returns
        --------
        float
            Inverse value which its cumulative probability is z..
        
        Note
        ----
        z argument must be a valid probability between 0 and 1
        """
        assert 0 < z < 1, f'{z} must be a valid probability between 0 and 1'
        return z*(self.b-self.a)+self.a


class Exponential():
    r"""Class for defining the Probability Density Function (PDF) of the Exponential distribution.

    The exponential probability distribution is computed as:

    $$f(x) = \left\lbrace\begin{array}{cc}(1/\lambda) * \exp(-x/\lambda),& if\;x\geq 0\\ 0,  &  \mathrm{otherwise}\end{array}\right.$$

    
    Parameters
    ----------
    param_lambda : float
        rate lambda parameter of the exponential distribution. It must be a positive real number.
    
    Note
    ----
    It uses the rate parameter definition. In case that lambda represents the scale parameter,
    initialize the distribution using 1/lambda.
    """

    def __init__(self, param_lambda):
        if (isinstance(param_lambda, str)):
            raise TypeError(f'{param_lambda} must be a positive real number')
        elif (param_lambda <= 0):
            raise ValueError(f'{param_lambda} must be a positive real number')
        else:
            self.param_lambda = param_lambda
            self.expectedValue = param_lambda
            self.variance = param_lambda**2

    def Density(self, x):
        r"""Compute Probability Density Function (PDF) of the Exponential distribution.
        
        $$f(x) = \left\lbrace\begin{array}{cc}(1/\lambda) * \exp(-x/\lambda),& if\;x\geq 0\\ 0,  &  \mathrm{otherwise}\end{array}\right.$$
        
        Parameters
        ----------
        x : float
            Point where the probability density function is evaluated.
        
        Returns
        ------
        float
            Probability density evaluated at x.

        Note
        ----

        The exponential distribution is defined by one parameter:
        rate parameter \lambda.

        The probability density has exponential shape when x>=0
        and zero when x<0.
        """
        if (x < 0):
            return 0
        else:
            return 1.0/self.param_lambda * exp(-x/self.param_lambda)

    def Distribution(self, x):
        r"""Compute the Cumulative Distribution Function(CDF) of the Exponential distribution.

        $$F(x) =\left\lbrace\begin{array}{cc}1-\exp(-x/\lambda), & x\geq 0, \\0, & x <0 \end{array}\right.$$
        
        Parameters
        ----------
        x : float
            Point where the Cumulative Distribution Function is evaluated.

        Returns
        --------
        float
            Cumulative probability up to x, i.e. $P(X\leq x)$.
        """
        if x < 0:
            return 0
        else:
            return 1.0 - exp(-x/self.param_lambda)

    def Probability(self, x, y):
        r"""Compute the Probability of the continuous Uniform distribution.

        Parameters
        ----------
        x : float
            Lower bound of the interval where the probability is computed.
        y : float
            Upper bound of the interval where the probability is computed.

        Returns
        --------
        float
            Probability of X belongs to intervals [x,y], i.e. $P(x \leq X \leq y)$.

        """
        if x > y:
            raise ValueError(f'{x} must be smaller than  {y}')
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        r"""Compute the inverse of the Exponential distribution.

        $$x=F^{-1}(z)$$
        
        Parameters
        ----------
        z : float
            Cumulative probability of the Exponential distribution, i.e., $P(X\leq x)=z$

        Returns
        --------
        float
            Inverse value which its Cumulative probability is z.
        
        Note
        ----
        z argument must be a valid probability between 0 and 1
        """
        assert 0 < z < 1, f'{z} must be a valid probability between 0 and 1'
        return -1.0*self.param_lambda*ln(1.0-z)


class Normal():
    r"""Class for defining the Probability Density Function (PDF) of the Normal distribution.

    Parameters
    ----------
    mean : float
        The localization(mean) parameter (denoted as $\mu$).
    varianza : float
        The scale(varianza) parameter (denoted as $\sigma^2$). Must be > 0.
    
    Note
    ----
    When mean or varianza are not given as argument, a Standard Normal distribution is assumed
    where mean=0 and varianza=1.
    """

    def __init__(self, mean=None, variance=None):
        if (variance != None and variance < 0):
            raise ValueError(f'Variance {variance} must be a positive value.')
        if (mean is None or variance is None):
            # When mean or variance are not given, the Standard Normal distribution is assumed
            mean = 0.0
            variance = 1.0
            print(
                f'Standard Normal distribution is assumed (mean = {mean} and variance = {variance})')
        # mu=mean
        self.mean = mean
        # sigma=(variance)^0.5
        self.standardDeviation = sqrt(variance)
        # Set expected and variance values
        self.expectedValue = mean
        self.variance = variance
        # normal factor defined for having a valid PDF
        self.normalFactor = 1.0/(SQRT_2*SQRT_PI*self.standardDeviation)

    def Density(self, x):
        r"""Compute Probability Density Function (PDF) of the Normal distribution.

        ----------
        x : float
            Point where the probability density function is evaluated.
        
        Returns
        ------
        float
            Probability density evaluated at x.
        """
        return self.normalFactor * exp(-0.5*((x-self.mean)/self.standardDeviation)**2)

    def Distribution(self, x):
        r"""Compute the Cumulative Distribution Function(CDF) of the Exponential distribution.

        $$F(x)=P(X\leq x)$$
        
        Parameters
        ----------
        x : float
            Point where the Cumulative Distribution Function is evaluated.

        Returns
        --------
        float
            Cumulative probability up to x, i.e. $$P(X\leq x)$$.
        
        Note
        ----
        The probability value is computed using the erf function defined in mathematics.py
        For more information, please read that file.
        """

        # normalization is applied $$Z=(x-\mu)/\sigma$$

        normalized_x = (x-self.mean)/(SQRT_2*self.standardDeviation)
        if x >= 0:
            return 0.5*(1 + erf(normalized_x))
        else:
            return 0.5*(1 - erf(-1.0*normalized_x))

    def Probability(self, x, y):
        r"""Compute the Probability of the Normal distribution.

        Parameters
        ----------
        x : float
            Lower bound of the interval where the probability is computed.
        y : float
            Upper bound of the interval where the probability is computed.

        Returns
        --------
        float
            Probability of X belongs to intervals [x,y], i.e. $P(x \leq X \leq y)$.

        """
        if x > y:
            raise ValueError(f'{x} must be smaller than {y}')
        elif x == y:
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

    def inv(self, z: float) -> float:
        r"""Compute the inverse of the Normal distribution.

        $$x=F^{-1}(z)$$
        
        Parameters
        ----------
        z : float
            Cumulative probability of the Normal distribution, i.e., $P(X\leq x)=z$

        Returns
        --------
        float
            Inverse value which its Cumulative probability is z.
        
        Note
        ----
        z argument must be a valid probability between 0 and 1.
        Newton-Raphson method is used as an iterative method for computing the fixed point
        of the equation $g(x)=F(x)-z=0$. $F(x)$ and $f(x)$ are needed for computing the inverse value.
        for more information, go to mathematics.py module.
        """
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
                f'{alpha} parameter must be an positive integer or half-integer')
        else:
            self.alpha = alpha
        if (beta is None):
            print("\n beta parameter is initialized to 1.0")
            self.beta = 1.0
        elif (beta < 0):
            raise ValueError(
                f'scale parameter {beta} must be bigger than zero')
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
            raise ValueError(f'{n} must be an integer bigger than zero')
        super().__init__(n/2, 2.0)

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing mathematics functions and constants needed for probability, statistics and others

"""

from typing import Any

PI = 3.1415926535897932
SQRT_PI=1.7724538509055159
SQRT_2=1.414213562373095
EULER = 2.7182818282861687

def procedure_to_base(x:float, b:int)->list:
    """
    Compute the representation of number n in the base b.

    Parameters
    ----------
    n : float
        number to be represented in base b.
    b : int
        base number.

    Returns
    -------
    list
        list of integers [a_1,a_2,..._a_k ] to represent n in base-b.
    """    
    a=[]
    while x != 0:
        a.append(x%b)
        x = x//b
    a.reverse()
    return a

def checkInteger(x):
    if (2*x-int(2*x))!= 0.0:
        return False
    return True

def factorial(k):
    n=k
    # define a flag for dealing with case when k=(2n-1)/2 is half of an integer value
    k_NonInT=False
    if (int(k)- n)!=0:
        # recompute n based of the hal-integer value k
        n=int((2*k+1)//2)
        # enable flag for half-integer values
        k_NonInT=True
    else:
        # for k to be integer( not a float)
        n=int(k)
    # Memoization, use list of size n+1 ([f[0],f[1],....,f[n]])
    F=[0.0]*(n+1)
    #  Handle base-Cases
    if k_NonInT:
        F[0]=sqrt(PI)
    else:
        F[0]=1.0
    # Filling up list to be look up
    for i in range(1,n+1):
        if k_NonInT:
            F[i]=((2*i-1)/2)*F[i-1]
        else:
            F[i]=i*F[i-1]
    
    return F[n]
    
def gamma(k:int|float)->int|float:
    """
    Compute gamma function given a real positive value.

    Parameters
    ----------
    k : int|float
        Real positive value where gamma function is computed.

    Returns
    -------
    int|float
        Approximation of gamma function of k.
    
    Notes
    -----
    The gamma function is computed using the Lanczos approximation for G=7 and n=9.
    Code has been adapted from the reference given below.
    https://en.wikipedia.org/wiki/Lanczos_approximation

    When k is an integer or half-integer (2n-1)/2, the identity Gamma(k)=(k-1)! is used.
    """
    assert k>0, f'Gamma function is not implemented for negative values.'

    # if k is and integer or half-integer, factorial function is used.
    if (checkInteger(k)):
        return factorial(k-1)

    # Implement Lanczos approximation.
    # Constant g and Coefficients p_k(g)
    G = 7
    P = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7
    ]

    if k < 0.5:
        # Lanczos is not valid for k smaller than 0.5. Reflection formula is used.
        return PI / (sine(PI * k) * gamma(1-k))
    k -= 1
    x = P[0] + sum(P[i] / (k + i) for i in range(1, len(P)))
    t = k + G + 0.5

    return sqrt(2 * PI) * t ** (k + 0.5) * exp(-t) * x

def cosine(x:float, n_sum:int=90, tol:float=10**-12)->float:
    """
    Compute the cosine of x using the Maclaurin series.

    Parameters
    ----------
    x : float
        Angle in radians.
    n_sum : int
        Maximum number of terms in the series.
    tol : float
        Absolute tolerance for convergence.

    Returns
    -------
    float
        Approximation of cos(x).
    """

    # Perform argument reduction to interval [-PI, PI]
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI

    # Use symmetry and reduce to interval [-PI/2, PI/2] for improving accuracy
    # Cosine is negative within the intervals [-PI,-PI/2] y [PI/2,PI], then sign-value is used.
    sign = 1.0
    if x > PI / 2:
        x = PI - x
        sign = -1.0
    elif x < -PI / 2:
        x = -PI - x
        sign = -1.0

    # First term of the MaClaurin series of cos(x)
    cosine_value = 1.0
    term_cosine = 1.0

    # Add additional terms to the serie
    for k in range(1, n_sum):
        term_cosine *= -(x**2) / ((2*k - 1)*(2*k))
        cosine_value += term_cosine

        if abs(term_cosine) < tol:
            break

    return sign * cosine_value


def sine(x:float, n_sum:int=90, tol:float=10**-12)->float:
    """
    Compute the sine of x using the Maclaurin series.

    Parameters
    ----------
    x : float
        Angle in radians.
    n_sum : int
        Maximum number of terms in the series.
    tol : float
        Absolute tolerance for convergence.

    Returns
    -------
    float
        Approximation of sin(x).
    """

    # Perform argument reduction to interval to [-PI, PI] using module
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
        
    # Reduce to [-PI/2, PI/2] using symmetry for improving accuracy
    if x > PI / 2:
        x = PI - x
    elif x < -PI / 2:
        x = -PI - x

    # first term of the MaClaurin series of sin(x)
    sine_value = x
    term_sine = x

    # Add additional terms to the serie
    for k in range(1, n_sum):
        term_sine *= -(x**2)/((2*k+1)*(2*k))
        sine_value += term_sine

        if abs(term_sine) < tol:
            break

    return sine_value

def exp(x:float, n_sum:int=90, tol:float=10**-12)->float:
    """
    Compute the exponential of x using the Maclaurin series.

    Parameters
    ----------
    x : float
        Point where exponential is evaluated.
    n_sum : int
        Maximum number of terms in the series.
    tol : float
        Absolute tolerance for convergence.

    Returns
    -------
    float
        Approximation of exp(x).
    """
    if x<0:
        return 1/exp(-x)
    exp_value=1.0
    term_exp=1.0
    for k in range(1,n_sum):
        term_exp*=x/k
        exp_value+=term_exp
        next_term = term_exp * x / (k + 1)
        ratio = abs(x) / (k + 2)

        if ratio < 1:
            error_bound = abs(next_term) / (1 - ratio)

            if error_bound < tol:
                break

    return exp_value


def ln(x: float) -> float:
    """
    Compute the logarithm of x using Newton-Raphson.

    Parameters
    ----------
    x : float
        Point where logarithm is evaluated.

    Returns
    -------
    float
        Approximation of ln(x).

    Note
    ----
    The method decompuses the number x as
    $$x=a* 10^{n}$$
    with *a* a value in the range [1,10), then it uses the logarithm property:
    $$\ln(x)=\ln(a)+n\ln(10)$$ # type: ignore
    and compute $\ln(a)$ using Newton-Raphson in the fixed-point formula $\exp(y/2)-x\exp(-y/2)=0$ 
    
    """

    # first represent x in base-10 representation and get the largest n such as x=a*10^n
    # with a in interval [1,10)]
    n = len(procedure_to_base(x, 10))-1
    # Divide x by 10^{n} to get a number in the range[1,10)
    a = x/(10**n)
    # Used ln(10) value for computing ln(x)
    ln_10 = 2.302585092994046
    # Get ln_a approximation using Newton-Raphson
    ln_a = Newton_Raphson(lambda y: -2*(a-exp(y)),
                          lambda y: a+exp(y), x_0=a/2, tol=10**-12, n_max=10)
    # return approximation of ln(x)
    return ln_a + (n*ln_10)


def sqrt(x:float,x_0=None, tol=10**-6, n_max=10)->float:
    """
    Compute the square root of x using Newton-Raphson.

    Parameters
    ----------
    x : float
        Point whose square root is going to be computed. It must be >=0

    Returns
    -------
    float
        Approximation of $$\sqrt{x}$$.

    Note
    ----
    The method computes $\sqrt{x}$ using Newton-Raphson in the fixed-point formula $y^2-x=0$ 
    
    """
    if (x<0):
        raise ValueError(str(x)+" must be a positive value")
    if (x==0):
        return 0
    if (x_0 is None):
        x_0=x/2
    return Newton_Raphson(lambda y: y**2-x,lambda y: 2*y, x_0=x_0,tol=tol,n_max=n_max)

def erf(x:float, n_sum=90, tol=10**-12)->float:
    int_value=0
    for k in range(0,n_sum+1):
        int_value_1 =int_value+((-1.0)**k)*x**(2*k+1)/((2*k+1)*factorial(k))
        error = abs(int_value_1-int_value)
        if (tol<=error):
            int_value=int_value_1
        else:
            break
    return (2/SQRT_PI)*int_value

def dotProduct(x:Any, y:Any)->float:
    assert len(x)==len(y), f'list of number does not have the same length ({len(x)} != {len(y)})!! '
    assert all(type(x[i])==int or type(x[i])==float for i in range(len(x))), "list x must be a list of numbers"
    assert all(type(y[i])==int or type(y[i])==float for i in range(len(y))), "list y must be a list of numbers"
    x_dot_y=0
    for i in range(len(x)):
        x_dot_y+=x[i]*y[i]
    return x_dot_y

def Newton_Raphson(func,func_prime,x_0:float,tol=10**-6, n_max=10)->float:
    """
    Template for Newton-Raphson iterative Method.

    Parameters
    ----------
    x_0 : float
        Initial guess for initiate iterations.
    func: lambda
        Lambda funcion which is the function which a root wants to be estimated $f(x)=0$.
    func_prime: lambda
        Lambda function which is the derivative of the function f(x)=0 which a root wants to be estimated.
    tol: float
        tolerance (precision) of the root estimation.
    n_max: int
        Maximum number of iterations for the Newton-Raphson. Method stops once $n_{max}$ is achieved.

    Returns
    -------
    float
        Root estimation of the equation f(x)=0.

    Note
    ----
    The method computes $\sqrt{x}$ using Newton-Raphson in the fixed-point formula $y^2-x=0$ 
    
    """
    error = 1
    n_iteration=0
    while (error>tol and n_iteration < n_max):
        x_1=x_0-func(x_0)/func_prime(x_0)
        error = abs((x_1-x_0)/x_0)
        x_0=x_1
        n_iteration+=1
        if (n_iteration==n_max):
            print("maximum number of iterations has been reached, with an error: ", error)
            break
    return x_0
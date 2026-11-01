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

def checkInteger(x):
    if (2*x-int(2*x))!= 0.0:
        raise ValueError(str(x)+" must be a non-negative integer or a half-integer n/2!!")

def factorial(k):
    # check that k must be a non-negative integer or a half-integer
    checkInteger(k)
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
    
def gamma(k):
    return factorial(k-1)

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
    cosine_value = 1.0
    term_cosine = 1.0

    for k in range(1, n_sum):
        term_cosine *= -(x**2) / ((2*k - 1)*(2*k))
        cosine_value += term_cosine

        if abs(term_cosine) < tol:
            break

    return cosine_value


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
    sine_value = x
    term_sine = x

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

def ln(x, n_sum=90, tol=10**-12):
    ln_value=0
    for k in range(0,n_sum+1):
        ln_value_1 =ln_value+2*((x-1)/(x+1))**(2*k+1)/(2*k+1)
        error = abs(ln_value_1-ln_value)
        if (tol<=error):
            ln_value=ln_value_1
        else:
            break
    return ln_value

def sqrt(x:float,x_0=None, tol=10**-6, n_max=10)->float:
    if (x<0):
        raise ValueError(str(x)+" must be a positive value")
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
    error = 1
    n_iteration=1
    while (error>tol and n_iteration < n_max):
        x_1=x_0-func(x_0)/func_prime(x_0)
        error = abs((x_1-x_0)/x_0)
        x_0=x_1
        n_iteration+=1
        if (n_iteration==n_max):
            print("maximum number of iterations has been reached, with an error: ", error)
            break
    return x_0
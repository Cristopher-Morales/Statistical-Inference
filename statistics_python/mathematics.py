# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing mathematics functions and constants needed for probability, statistics and others

"""

PI = 3.1415926535897932
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
    F=[0]*(n+1)
    #  Handle base-Cases
    if k_NonInT:
        F[0]=sqrt(PI)
    else:
        F[0]=1
    # Filling up list to be look up
    for i in range(1,n+1):
        if k_NonInT:
            F[i]=((2*i-1)/2)*F[i-1]
        else:
            F[i]=i*F[i-1]
    
    return F[n]
    
def gamma(k):
    return factorial(k-1)

def cosine(x, n_sum=90, tol=10**-12):
    cosine_value=0
    for k in range(0,n_sum):
        cosine_value_1=cosine_value+(-1)**k*x**(2*k)/factorial(2*k)
        if abs(cosine_value_1-cosine_value)>tol:
            cosine_value=cosine_value_1
        else:
            break
    return cosine_value

def sine(x, n_sum=90, tol=10**-12):
    sine_value=0
    for k in range(0,n_sum):
        sine_value_1=sine_value+(-1)**k*x**(2*k+1)/factorial(2*k+1)
        if abs(sine_value_1-sine_value)>tol:
            sine_value=sine_value_1
        else:
            break
    return sine_value

def exp(x, n_sum=90, tol=10**-12):
    exp_value=0
    for k in range(0,n_sum+1):
        exp_value_1 =exp_value+x**k/factorial(k)
        error = abs(exp_value_1-exp_value)
        if (tol<=error):
            exp_value=exp_value_1
        else:
            break
    return exp_value

def compute_pi(n_division=None):
    if n_division is None:
        n_division=100
    h=1/n_division
    pi_value=0
    for i in range(0,n_division+1):
        pi_value+=2*sqrt(1-(-1+i*2*h)**2)*2*h
    return pi_value

def sqrt(x,x_0=None, tol=10**-6, n_max=10):
    if (x<0):
        raise ValueError(str(x)+" must be a positive value")
    if (x_0 is None):
        x_0=x/2
    error = 1
    n_iteration=1
    while (error>tol and n_iteration < n_max):
        x_1=(x_0+x/x_0)/2
        error = abs((x_1-x_0)/x_0)
        x_0=x_1
        n_iteration+=1
        if (n_iteration==n_max):
            print("maximum number of iterations has been reached, with an error: ", error)
    return x_0

def compute_integral_exp2(x, n_sum=90, tol=10**-12):
    int_value=0
    for k in range(0,n_sum+1):
        int_value_1 =int_value+((-1.0)**k)*x**(2*k+1)/((2*k+1)*factorial(k)*2**k)
        error = abs(int_value_1-int_value)
        if (tol<=error):
            int_value=int_value_1
        else:
            break
    return int_value

def dotProduct(x:list, y:list)->float:
    assert len(x)==len(y), "list of number does not have the same length!!"
    assert all(type(x[i])==int or type(x[i])==float for i in range(len(x))), "list x must be a list of numbers"
    assert all(type(y[i])==int or type(y[i])==float for i in range(len(y))), "list y must be a list of numbers"
    x_dot_y=0
    for i in range(len(x)):
        x_dot_y+=x[i]*y[i]
    return x_dot_y
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal
"""
import numpy as np
from probability import factorial

PI = 3.141592653589793
EULER = 2.7182818282861687

def cosine(x):
    cosine_value=0
    for k in range(0,31):
        cosine_value+=(-1)**k*x**(2*k)/factorial(2*k)
    return cosine_value

def sine(x):
    sine_value=0
    for k in range(0,31):
        sine_value+=(-1)**k*x**(2*k+1)/factorial(2*k+1)
    return sine_value

def exp(x, n_sum=None, tol=None):
    if (n_sum==None):
        n_sum = 60
    if (tol==None):
        tol=10**-9
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
        n_division=30
    h=1/n_division
    pi_value=0
    for i in range(0,n_division+1):
        pi_value+=2*np.sqrt(1-(-1+i*2*h)**2)*2*h
    return pi_value

def sqrt(x,x_0=None, tol=None, n_max=None):
    if (x<0):
        raise ValueError(str(x)+" must be a positive value")
    if (tol == None):
        tol = 10**-6
    if (n_max ==None):
        n_max = 10
    if (x_0 == None):
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

# print(sqrt(0.5))
# print(sqrt(25))
# print(cosine(np.pi), np.cos(np.pi))
# print(sine(np.pi/2), np.sin(np.pi/2))
# print(exp(1), np.exp(1))
# print(len([1,2,3]))
# print(compute_pi(100000), np.pi)

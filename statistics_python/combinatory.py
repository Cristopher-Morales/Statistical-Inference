"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module for implementing combinatory quantities needed for probabilities distributions

"""
from mathematics import factorial

def permutation(n,k):
    if n>=k:
        return factorial(n)/factorial(n-k)
    else:
        raise ValueError("n must be bigger or equal than k")
def combination(n,k):
    if n>=k:
        return permutation(n,k)/factorial(k)
    else:
        raise ValueError("n must be bigger or equal than k")
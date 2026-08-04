"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module for implementing combinatory quantities needed for probabilities distributions

"""
from mathematics import factorial

def permutation(n:int,k:int)->int:
    assert isinstance(n, int) and isinstance(k, int), f'{n} and {k} must be integers bigger or equal than zero.'
    assert n>=0 and k>=0, f'{n} and {k} must be integers bigger or equal than zero.'
    assert (n>=k), f'{n} must be bigger or equal than {k} for computing a valid permutation.'

    return int(factorial(n)/factorial(n-k))
    
def combination(n:int,k:int)->int:
    assert isinstance(n, int) and isinstance(k, int), f'{n} and {k} must be integers bigger or equal than zero.'
    assert n>=0 and k>=0, f'{n} and {k} must be integers bigger or equal than zero.'
    assert (n>=k), f'{n} must be bigger or equal than {k} for computing a valid combination.'

    return int(permutation(n,k)/factorial(k))
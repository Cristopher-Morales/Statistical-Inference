"""
Created on Wed July 15 13:29 2026

@author: Cristopher Morales Ubal

Module implementing iterative methods.

"""

from mathematics import dotProduct

def GauusSeidel_Method(A:list, b:list, tol:float=10**-6, n_max_iter:int=30, x_initial:list=None)->list:
    n=len(A[0])
    assert len(A[0])==len(A), "works only for square matrices!! please check your matrix"
    assert len(b)==len(A[0]), "right-had size vector b must have the same number of rows as matrix A"
    # initial guess
    if (x_initial==None) : x_initial=[1]*len(A)
    # initialize 
    n_count=1
    error=1.0
    x_1=[0]*len(A)
    x_0=x_initial.copy()
    while (error>=tol and n_count<=n_max_iter):
        x_1[0]=(1/A[0][0])*(b[0]-dotProduct(A[0][1:],x_0[1:]))
        for j in range(1,n-1):
            x_1[j]=(1/A[j][j])*(b[j]-dotProduct(A[j][j+1:],x_0[j+1:])-dotProduct(A[j][:j],x_1[:j]))
        x_1[n-1]=(1/A[n-1][n-1])*(b[n-1]-dotProduct(A[n-1][:n-1],x_1[:n-1]))
        error=max([abs(x_1[i]-x_0[i]) for i in range(n)])
        x_0=x_1.copy()
        if (n_count==n_max_iter):
            print("maximum number of iterations has been reached")
            break
        n_count+=1
    return x_1, n_count, error

def Jacobi_Method(A:list, b:list, tol:float=10**-6, n_max_iter:int=30, x_initial:list=None)->list:
    n=len(A[0])
    assert len(A[0])==len(A), "works only for squared matrices!! please check your matrix"
    assert len(b)==len(A[0]), "right-had size vector b must have the same number of rows as matrix A"
    # initial guess
    if (x_initial==None) : x_initial=[1]*len(A)
    # initialize 
    n_count=1
    error=1.0
    x_1=[0]*len(A)
    x_0=x_initial.copy()
    while (error>=tol and n_count<=n_max_iter):
        for j in range(n):
            x_1[j]=(1/A[j][j])*(b[j]-dotProduct(A[j],x_0)+A[j][j]*x_0[j])
        error=max([abs(x_1[i]-x_0[i]) for i in range(n)])
        x_0=x_1.copy()
        if (n_count==n_max_iter):
            print("maximum number of iterations has been reached")
            break
        n_count+=1
    return x_1, n_count, error
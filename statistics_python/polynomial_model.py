"""
Created on Wed July 15 13:29 2026

@author: Cristopher Morales Ubal

Module implementing class for polynomial fitting.

"""
from matrix import *

class PolynomialModel():
    def __init__(self, n_degree:int=1):
        assert  n_degree>=1  and type(n_degree) is int, f'polynomial degree must be an integer bigger or equal than one, invalid value {n_degree}.'
        if (n_degree is None): print("polynomial degree is initializes to 1.0")
        self.n_degree = n_degree
        self._x=[]
        self._y=[]
        self.NormalMatrix=None
        self._rhsVector=None
        self.coefficient=[]*n_degree
    
    def set_data(self, x: list, y: list):
        assert len(x)==len(y), f'input and output must have the same lenght, currently lenght(x) is {len(x)} and lenght(y) is {len(y)}.'
        self._x=x
        self._y=y
    
    def fit_model(self):
        self.ComputeMatrices()
        NormalMatrixInverse=self.NormalMatrix.inverse()
        self.coefficient=NormalMatrixInverse*self._rhsVector

    def predict(self,inputs:list):
        coeffs_list=self.coefficient.transpose()._Matrix
        y_outputs=[sum([a*x**j for (j,a) in enumerate(coeffs_list[0])]) for x in inputs]
        return y_outputs    
    
    def ComputeMatrices(self):
        m=len(self._x)
        n_normal=self.n_degree+1
        X=Matrix(rows=m, columns=n_normal)
        Y=Matrix(rows=m, columns=1)
        for i in range(m): X[i,0]= 1
        for i in range(m):
            for j in range(n_normal):
                X[i,j]=self._x[i]**j
        for j in range(m):
            Y[j,0]=self._y[j]
        X_T=X.transpose()
        self.NormalMatrix=X_T*X
        self._rhsVector=X_T*Y

model_1=PolynomialModel(2)
x=[1, 2, 3, 4, 5,6,7]
y=[50,55,65,80,110,150,200]
model_1.set_data(x,y)
model_1.fit_model()
print(model_1.coefficient)
y_outputs=model_1.predict(x)
print(y)
print(y_outputs)
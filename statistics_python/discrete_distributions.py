"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing classes for discrete distributions commonly used in statistics, probability, machine learning and others.

"""

from mathematics import exp
from combinatory import factorial, combination

class Binomial():

    def __init__(self,n,p):
        if (isinstance(n,int)!= True or n<0):
            raise TypeError(str(n)+" must be a positive integer bigger than zero")
        if (p<0 or p>1):
            raise ValueError(str(p)+" must a valid probability between zero and one")
        self.n=n
        self.p=p
        self.expectedValue= n*p
        self.variance= n*p*(1-p)
    def MassProbability(self, x):
        if isinstance(x,int)!= True or x < 0:
            raise ValueError(str(x)+" must be an integer bigger or equal than 0")
        if self.n>=x:
            return combination(self.n,x)*(self.p**x)*(1-self.p)**(self.n-x)
        else:
            raise ValueError(str(x)+" must be equal or smaller than the number of trials "+str(self.n))
    def Distribution(self,x):
        if isinstance(x,int)!= True:
            raise ValueError(str(x)+" must be an integer bigger or equal than 0")
        prob = 0
        for k in range(0,min(self.n+1,x+1)):
            prob+= Binomial.MassProbability(self, k)
        return prob
    def Probability(self,a,b):
        if isinstance(a,int)!= True  or isinstance(b,int)!=True:
            raise ValueError(str(a)+","+str(b)+" must be integers bigger or equal than zero, and "+str(a)+"<"+str(b))
        elif (a>=b):
            raise ValueError(str(a)+" must be smaller than b, if "+str(a)+"="+str(b)+" use poissonMassProbability method")
        if a>0:
            return Binomial.Distribution(self,b)-Binomial.Distribution(self, a-1)
        else:
            return Binomial.Distribution(self,b)

class Geometric:
    def __init__(self, geometric_param):
        if (geometric_param == None or geometric_param < 0):
            raise ValueError(str(geometric_param)+ " must be a positive value different than zero")
        self.geometric_param=geometric_param
        self.expectedValue= 1.0/geometric_param
        self.variance= (1.0 - geometric_param ) / geometric_param**2
    def MassProbability(self, x):
        if isinstance(x,int)!= True or x < 1:
            raise ValueError(str(x)+" must be an integer bigger or equal than 1")
        return self.geometric_param * (1-self.geometric_param)**(x-1)
    def Distribution(self,x):
        if isinstance(x,int)!= True:
            raise ValueError(str(x)+" must be an integer bigger or equal than 1")
        prob = 0
        for k in range(1,x+1):
            prob+= Geometric.MassProbability(self, k)
        return prob
    def Probability(self,a,b):
        if isinstance(a,int)!= True  or isinstance(b,int)!=True:
            raise ValueError(str(a)+","+str(b)+" must be integers bigger or equal than 1, and "+str(a)+"<"+str(b))
        elif (a>=b):
            raise ValueError(str(a)+" must be smaller than b, if "+str(a)+"="+str(b)+" use poissonMassProbability method")
        if a>1:
            return Geometric.Distribution(self,b)-Geometric.Distribution(self, a-1)
        else:
            return Geometric.Distribution(self,b)

class NegBinomial:
    def __init__(self, r, p):
        if (isinstance(r,int)!= True or r<1):
            raise TypeError("the number of success wanted "+str(r)+" must be a positive integer bigger or equal than one")
        if (p<0 or p>1):
            raise ValueError(str(p)+" must a valid probability between zero and one")
        self.r = r
        self.p = p
        self.expectedValue= self.r*(1-self.p)/self.p
        self.variance= self.expectedValue/self.p
    def MassProbability(self, x):
        if isinstance(x,int)!= True or x < self.r:
            raise ValueError(str(x)+" must be an integer bigger or equal than the number of success wanted "+str(self.r))
        return combination(x-1, self.r-1) *self.p**self.r * (1-self.p)**(x-self.r)
    def Distribution(self,x):
        if isinstance(x,int)!= True:
            raise ValueError(str(x)+" must be an integer bigger or equal than the wanted success "+str(self.r))
        prob = 0
        for k in range(self.r,x+1):
            prob+= NegBinomial.MassProbability(self, k)
        return prob
    def Probability(self,a,b):
        if isinstance(a,int)!= True  or isinstance(b,int)!=True:
            raise ValueError(str(a)+","+str(b)+" must be integers bigger or equal than 1, and "+str(a)+"<"+str(b))
        elif (a>=b):
            raise ValueError(str(a)+" must be smaller than b, if "+str(a)+"="+str(b)+" use poissonMassProbability method")
        if a>self.r:
            return NegBinomial.Distribution(self,b)-NegBinomial.Distribution(self, a-1)
        else:
            return NegBinomial.Distribution(self,b)

class Poisson:
    def __init__(self, poison_param):
        if (poison_param == None or poison_param < 0):
            raise ValueError(str(poison_param)+ " must be a positive value different than zero")
        self.poison_param=poison_param
        self.expectedValue= poison_param
        self.variance= poison_param
    def MassProbability(self, x):
        if isinstance(x,int)!= True:
            raise ValueError(str(x)+" must be an integer bigger or equal than zero")
        return exp(-1* self.poison_param) * self.poison_param**x / factorial(x)
    def Distribution(self,x):
        if isinstance(x,int)!= True:
            raise ValueError(str(x)+" must be an integer bigger or equal than zero")
        prob = 0
        for k in range(0,x+1):
            prob+= Poisson.MassProbability(self, k)
        return prob
    def Probability(self,a,b):
        if isinstance(a,int)!= True  or isinstance(b,int)!=True:
            raise ValueError(str(a)+","+str(b)+" must be integers bigger or equal than zero, and "+str(a)+"<"+str(b))
        elif (a>=b):
            raise ValueError(str(a)+" must be smaller than b, if "+str(a)+"="+str(b)+" use poissonMassProbability method")
        if a>0:
            return Poisson.Distribution(self,b)-Poisson.Distribution(self, a-1)
        else:
            return Poisson.Distribution(self,b)
    
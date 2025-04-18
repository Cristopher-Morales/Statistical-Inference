"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing classes for continuous distributions commonly used in statistics, probability, machine learning and others.

"""

from mathematics import PI, exp, sqrt, compute_integral_exp2, gamma

class Uniform():

    def __init__(self,a,b):
        if (isinstance(a,str) or isinstance(b,str)):
            raise TypeError(str(a)+","+str(b)+" must be real number, and "+str(a)+"<"+str(b))
        if (b<=a):
            raise ValueError(str(a)+" must be smaller than "+str(b))
        self.a=a
        self.b=b
        self.expectedValue= (a+b)/2
        self.variance= (b-a)**2/12
    def Density(self, x):
        if (x<=self.a or x>=self.b):
            return 0
        else:
            return 1.0/(self.b-self.a)
    def Distribution(self,x):
        if x<self.a:
            return 0
        elif self.a<=x or x<self.b:
            return (x-self.a)/(self.b-self.a)
        else:
            return 1
    def Probability(self,x,y):
        if x>y:
            raise ValueError(str(x)+" must be smaller than " +str(y))
        elif x==y :
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

class Exponential():

    def __init__(self,param_lambda):
        if (isinstance(param_lambda,str)):
            raise TypeError(str(param_lambda)+" must be real number")
        self.param_lambda=param_lambda
        self.expectedValue= param_lambda
        self.variance= param_lambda**2
    def Density(self, x):
        if (x<0):
            return 0
        else:
            return 1.0/self.param_lambda * exp(-x/self.param_lambda)
    def Distribution(self,x):
        if x<0:
            return 0
        else:
            return 1.0 - exp(-x/self.param_lambda)
    def Probability(self,x,y):
        if x>y:
            raise ValueError(str(x)+" must be smaller than " +str(y))
        elif x==y :
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

class Normal():

    def __init__(self, mean=None, variance=None):
        if (variance !=None and variance<0):
            raise ValueError("Variance "+str(variance)+" must be a positive value.")
        if (mean is None or variance is None):
            mean = 0.0
            variance = 1.0
        self.mean=mean
        self.standardDeviation=sqrt(variance)
        self.expectedValue=mean
        self.variance=variance
        self.normalFactor=1.0/sqrt(2*PI*variance)

    def Density(self, x):
        return self.normalFactor * exp(-0.5*((x-self.mean)/self.standardDeviation)**2)
    def Distribution(self,x):
        if x>=0:
            return 0.5 + self.normalFactor*compute_integral_exp2((x-self.mean)/self.standardDeviation)
        else:
            return 0.5 - self.normalFactor*compute_integral_exp2(-1.0*(x-self.mean)/self.standardDeviation)
    def Probability(self,x,y):
        if x>y:
            raise ValueError(str(x)+" must be smaller than " +str(y))
        elif x==y :
            return 0
        else:
            return self.Distribution(y)-self.Distribution(x)

class Gamma():

    def __init__(self, alpha, beta=None):
        if(alpha is None or (2*alpha-int(2*alpha)!=0)):
            raise ValueError("alpha parameter must be an positive integer or half-integer")
        else:
            self.alpha= alpha
        if(beta is None):
            print("\n beta values is initialized to 1.0")
            self.beta=1.0
        else:
            self.beta=beta
        self.expectedValue = self.alpha/self.beta
        self.variance=self.expectedValue/self.beta
        self.gammaFactor = self.beta**self.alpha/gamma(self.alpha)

    def Density(self, x):
        return self.gammaFactor * exp(-self.beta * x)*x**(self.alpha-1.0)

class chiSquared(Gamma):

    def __init__(self, n):
        if (isinstance(n,int)==False or n<=0):
            raise ValueError(str(n)+" must be an integer bigger than zero")
        super().__init__(n/2, 0.5)
        
    
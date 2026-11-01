"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module implementing classes for discrete distributions commonly used in statistics, probability, machine learning and others.

"""

from mathematics import exp
from combinatory import factorial, combination


class Binomial():

    def __init__(self, n_trials, prob):
        if (isinstance(n_trials, int) != True or n_trials < 0):
            raise TypeError(
                str(n_trials)+" must be a positive integer bigger than zero")
        if (prob < 0 or prob > 1):
            raise ValueError(
                str(prob)+" must a valid probability between zero and one")
        self.n = n_trials
        self.p = prob
        self.expectedValue = self.n*self.p
        self.variance = self.n*self.p*(1-self.p)

    def MassProbability(self, x):
        if isinstance(x, int) != True or x < 0:
            raise ValueError(
                str(x)+" must be an integer bigger or equal than 0")
        if self.n >= x:
            return combination(self.n, x)*(self.p**x)*(1-self.p)**(self.n-x)
        else:
            raise ValueError(
                str(x)+" must be equal or smaller than the number of trials "+str(self.n))

    def Distribution(self, x):
        if isinstance(x, int) != True:
            raise ValueError(
                str(x)+" must be an integer bigger or equal than 0")
        prob = 0
        for k in range(0, min(self.n+1, x+1)):
            prob += self.MassProbability(k)
        return prob

    def Probability(self, a, b):
        if isinstance(a, int) != True or isinstance(b, int) != True:
            raise ValueError(str(
                a)+","+str(b)+" must be integers bigger or equal than zero, and "+str(a)+"<"+str(b))
        elif (a >= b):
            raise ValueError(str(a)+" must be smaller than b, if " +
                             str(a)+"="+str(b)+" use poissonMassProbability method")
        if a > 0:
            return self.Distribution(b)-self.Distribution(a-1)
        else:
            return self.Distribution(b)


class Geometric:

    def __init__(self, prob):
        if (prob == None or prob < 0):
            raise ValueError(
                f'{prob} must be a positive value different than zero')
        self.prob = prob
        self.expectedValue = 1.0/prob
        self.variance = (1.0 - prob) / prob**2

    def MassProbability(self, x):
        if isinstance(x, int) != True:
            raise ValueError(f'{x} must be an integer bigger or equal than 1')
        if x < 1:
            return 0

        return self.prob * (1-self.prob)**(x-1)

    def Distribution(self, x):
        if isinstance(x, int) != True:
            raise ValueError(f'{x} must be an integer bigger or equal than 1')
        if x < 1:
            return 0
        prob = 0
        for k in range(1, x+1):
            prob += self.MassProbability(k)
        return prob

    def Probability(self, a, b):
        if isinstance(a, int) != True or isinstance(b, int) != True:
            raise ValueError(str(
                a)+","+str(b)+" must be integers bigger or equal than 1, and "+str(a)+"<"+str(b))
        elif (a >= b):
            raise ValueError(str(a)+" must be smaller than b, if " +
                             str(a)+"="+str(b)+" use poissonMassProbability method")
        if a > 1:
            return self.Distribution(b)-self.Distribution(a-1)
        else:
            return self.Distribution(b)


class NegBinomial:

    def __init__(self, n_success, prob):
        if (isinstance(n_success, int) != True or n_success < 1):
            raise TypeError("the number of success wanted "+str(n_success) +
                            " must be a positive integer bigger or equal than one")
        if (prob < 0 or prob > 1):
            raise ValueError(
                str(prob)+" must a valid probability between zero and one")
        self.r = n_success
        self.p = prob
        self.expectedValue = self.r*(1-self.p)/self.p
        self.variance = self.expectedValue/self.p

    def MassProbability(self, x):
        if isinstance(x, int) != True or x < self.r:
            raise ValueError(str(
                x)+" must be an integer bigger or equal than the number of success wanted "+str(self.r))
        return combination(x-1, self.r-1) * self.p**self.r * (1-self.p)**(x-self.r)

    def Distribution(self, x):
        if isinstance(x, int) != True:
            raise ValueError(
                str(x)+" must be an integer bigger or equal than the wanted success "+str(self.r))
        prob = 0
        for k in range(self.r, x+1):
            prob += self.MassProbability(k)
        return prob

    def Probability(self, a, b):
        if isinstance(a, int) != True or isinstance(b, int) != True:
            raise ValueError(str(
                a)+","+str(b)+" must be integers bigger or equal than 1, and "+str(a)+"<"+str(b))
        elif (a >= b):
            raise ValueError(str(a)+" must be smaller than b, if " +
                             str(a)+"="+str(b)+" use poissonMassProbability method")
        if a > self.r:
            return self.Distribution(b)-self.Distribution(a-1)
        else:
            return self.Distribution(b)


class Poisson:
    
    def __init__(self, poisson_param):
        if (poisson_param == None or poisson_param < 0):
            raise ValueError(str(poisson_param) +
                             " must be a positive value different than zero")
        self.poisson_param = poisson_param
        self.expectedValue = poisson_param
        self.variance = poisson_param

    def MassProbability(self, x):
        if isinstance(x, int) != True:
            raise ValueError(
                str(x)+" must be an integer bigger or equal than zero")
        return exp(-1 * self.poisson_param) * self.poisson_param**x / factorial(x)

    def Distribution(self, x):
        if isinstance(x, int) != True:
            raise ValueError(
                str(x)+" must be an integer bigger or equal than zero")
        prob = 0
        for k in range(0, x+1):
            prob += self.MassProbability(k)
        return prob

    def Probability(self, a, b):
        if isinstance(a, int) != True or isinstance(b, int) != True:
            raise ValueError(str(
                a)+","+str(b)+" must be integers bigger or equal than zero, and "+str(a)+"<"+str(b))
        elif (a >= b):
            raise ValueError(str(a)+" must be smaller than b, if " +
                             str(a)+"="+str(b)+" use poissonMassProbability method")
        if a > 0:
            return self.Distribution(b)-self.Distribution(a-1)
        else:
            return self.Distribution(b)

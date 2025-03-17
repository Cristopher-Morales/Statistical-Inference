from mathematics import exp
from probability import factorial

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

# obj =Poisson(2)
# print(obj.expectedValue)
# mass_prob_1 = obj.MassProbability(1)
# dist_prob = obj.Distribution(1)
# mass_prob_2 =obj.MassProbability(2)
# probability = obj.Probability(1,2)
# print(mass_prob_1, mass_prob_2,mass_prob_1+mass_prob_2, probability)
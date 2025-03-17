
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

# obj =Geometric(0.1)
# print(obj.expectedValue)
# mass_prob_1 = obj.MassProbability(1)
# dist_prob = obj.Distribution(1)
# mass_prob_2 =obj.MassProbability(2)
# probability = obj.Probability(1,2)
# print(mass_prob_1, mass_prob_2,mass_prob_1+mass_prob_2, probability)
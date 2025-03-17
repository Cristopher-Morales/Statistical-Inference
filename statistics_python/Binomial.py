from probability import combination

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
        
    
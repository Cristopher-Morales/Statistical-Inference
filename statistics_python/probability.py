#module for computing probability quantities
#from mathematics import PI

def checkInteger(x):
    if isinstance(x, int)!=True:
        raise ValueError(str(x)+" must be an Integer")

def factorial(k):
    checkInteger(k)
    if k>0:
        return k*factorial(k-1)
    elif (k==0):
        return 1
    else:
        raise ValueError("Number must non-negative!!")

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
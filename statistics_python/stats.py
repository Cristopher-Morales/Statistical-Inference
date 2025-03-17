#module for computing statistics indicators
from mathematics import sqrt

def mean_value(values=None):
    ''' 
    list::values: list containing the values from where the mean value will be computed
    '''
    '''start checks'''
    if (values==None or values==[]):
        raise ValueError("argument must be a non-empty list")
    elif(type(values)==str):
        raise TypeError("argument must be a list or a number")
    elif(type(values)==float or type(values)==int):
        values=[values]
    n = len(values)
    if n>1:
        return (n-1)*mean_value(values[:n-1])/n + values[n-1]/n
    else:
        return values[0]

def variance(values):
    mean = mean_value(values)
    variance = 0
    for i in range(0,len(values)):
        variance+=(values[i]-mean)**2
    return variance/len(values)

def std_deviation(values):
    return sqrt(variance(values))
    
# print(mean_value([1,1,3,5,5]))
# print(variance([1,1,3,5,5]))
# print(std_deviation([1,1,3,5,5]))
# #print(mean_value(1))
# #print(mean_value([]))
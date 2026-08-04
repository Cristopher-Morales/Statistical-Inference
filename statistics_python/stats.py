"""
Created on Wed Mar 12 18:34:49 2025

@author: Cristopher Morales Ubal

Module for implementing statistics quantities requiered for statistical inference

"""

from mathematics import sqrt

def mean_value(values=None)->float:
    ''' 
    list::values: list containing the values from where the mean value will be computed
    '''
    '''start checks'''
    if (values==None or values==[]):
        raise ValueError("argument must be a non-empty list of numbers or a single numerical value")
    elif(type(values)==str):
        raise TypeError("argument must be a list of numbers or a single number")
    elif(type(values)==float or type(values)==int):
        values=[values]
    n = len(values)
    if n>1:
        return (n-1)*mean_value(values[:n-1])/n + values[n-1]/n
    else:
        return values[0]

def variance(values:list)->float:
    ''' Variance computed using online algorithm (1-step) proposed by West (1979)'''
    if (values==None or values==[]):
        raise ValueError("argument must be a non-empty list of numbers or a single numerical value")
    elif(type(values)==str):
        raise TypeError("argument must be a list of numbers or a single number")
    elif(type(values)==float or type(values)==int):
        values=[values]
    mean =values[0]
    T = 0
    for i in range(1,len(values)):
        delta = (values[i]-mean)/(i+1)
        mean+=delta
        T+=(i+1)*i*delta**2
    return T/len(values)

def std_deviation(values:list)->float:
    return sqrt(variance(values))

def r2_coeff(y_true:list, y_pred:list)->float:
    assert isinstance(y_pred,list) and isinstance(y_true,list), f'{y_pred} and {y_true} must be valid list.'
    assert len(y_pred)==len(y_true), f'{y_pred} and {y_true} must have the same number of elements!!'
    SS_res=sum((y_pred_i-y_i)**2 for (y_pred_i,y_i) in zip(y_pred,y_true))
    SS_total=len(y_true)*variance(y_true)
    return 1-SS_res/SS_total
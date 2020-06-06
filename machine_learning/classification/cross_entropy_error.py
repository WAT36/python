import numpy as np
from logistic_regression import logistic_regression

#交差エントロピー誤差
def cross_entropy_error(w,x,t):
    y=logistic_regression(w,x)
    cee=0
    for n in range(len(y)):
        cee -= (t[n]*np.log(y[n]) + (1-t[n])*np.log(1-y[n]))
    return cee


#平均交差エントロピー誤差
def ave_cross_entropy_error(w,x,t):
    return cross_entropy_error(w,x,t)/len(x)

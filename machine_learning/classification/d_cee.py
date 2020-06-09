import numpy as np
from logistic_regression import logistic_regression

#平均交差エントロピー誤差の微分
def d_cee(w,x,t):
    y = logistic_regression(w,x)
    d_cee=np.zeros(2)
    for n in range(len(y)):
        #w0
        d_cee[0]+=(y[n]-t[n])*x[n]
        #w1
        d_cee[1]+=y[n]-t[n]
    d_cee /= len(y)
    return d_cee



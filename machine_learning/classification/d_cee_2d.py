import numpy as np
from logistic_regression_2d import logistic_regression_2d

#平均交差エントロピー誤差の微分(２次元入力)
def d_cee_2d(w,x,t):
    y = logistic_regression_2d(w,x)
    d_cee=np.zeros(3)
    for n in range(len(y)):
        #w0
        d_cee[0]+=(y[n]-t[n])*x[:,0]
        #w1
        d_cee[1]+=(y[n]-t[n])*x[:,1]
        #w2
        d_cee[2]+=y[n]-t[n]
    d_cee /= len(y)
    return d_cee



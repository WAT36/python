import numpy as np

def logistic_regression_2d(w,x):
    y = 1 / (1 + np.exp(-(w[0]*x[0] + w[1]*x[1] + w[2])))
    return y

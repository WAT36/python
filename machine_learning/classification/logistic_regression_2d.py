import numpy as np
from sigmoid import sigmoid

#ロジスティック回帰モデル(２次元入力)
def logistic_regression_2d(w,x):
    x = w[0]*x[:,0] + w[1]*x[:,1] + w[2]
    return sigmoid(x)

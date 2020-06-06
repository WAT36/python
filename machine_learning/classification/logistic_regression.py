import numpy as np
from sigmoid import sigmoid

#ロジスティック回帰モデル
def logistic_regression(w,x):
    x=w[0]*x + w[1]
    return sigmoid(x)

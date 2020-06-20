from sigmoid import sigmoid
import numpy as np

#ロジスティック回帰モデル(２次元入力)
def logistic_regression_2d(w,x):
    x = w[0]*x[:,0] + w[1]*x[:,1] + w[2]
    return sigmoid(x)

#ロジスティック回帰モデル(２次元入力・プロット用)
def logistic2d_for_plot(w,x0,x1):
    x = w[0]*x0 + w[1]*x1 + w[2]
    return sigmoid(x)


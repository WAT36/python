import numpy as np

#ロジスティック回帰モデル(２次元入力３クラス分類)
def logistic_regression_2d_3class(w,x):
    #w:3*3行列
    #x:n*2行列 (xの転置)
    n=len(x)
    #a:n*3行列
    a=np.zeros((n,3))
    for k in range(3):
        a[:,k] = np.exp( w[k,0]*x[:,0] + w[k,1]*x[:,1] +w[k,2] )
    #u:n*1行列、aの１行の要素の合計
    u = np.sum(a,axis=1)
    y = a/u
    return y



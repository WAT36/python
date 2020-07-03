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


#平均交差エントロピー誤差（２次元入力３クラス分類用）
def cross_entropy_error_for_2d_3class(w,x,t):
    #w:3*3行列
    #x:n*2行列（xの転置）
    #t:n*3行列（t[i]がクラスkにb分類された時t[i.k]=1,それ以外は0）
    y=logistic_regression_2d_3class(w,x)
    N=y.shape[0]
    #cee:平均交差エントロピー誤差
    cee=0
    for n in range(N):
        for k in range(3):
            cee = cee - (t[n,k] * np.log(y[n,k]))
    cee = cee / N
    return cee


#平均交差エントロピー誤差の偏微分（２次元入力３クラス分類用）
def d_cee_for_2d_3class(w,x,t):
    #w:3*3行列
    #x:n*2行列（xの転置）
    #t:n*3行列（t[i]がクラスkにb分類された時t[i.k]=1,それ以外は0）
    y=logistic_regression_2d_3class(w,x)
    #d_cee:3*3 (クラスの数k*(xの次元+1)) 行列
    d_cee=np.zeros((3,3))
    N=x.shape[0]
    for n in range(N):
        for k in range(3):
            d_cee[k,:] = d_cee[k,:] + (y[n,k]-t[n,k])*np.array(x[n,:]+[1])
    d_cee = d_cee / N
    return d_cee





import numpy as np
#ガウス関数 (式(2))
def gauss(x,mu,v):
    return np.exp(-(x-mu)**2/(2* v**2))


#線形基底関数モデル (式(1))
def linear_basis_func(w,x,mu,v):
    y=np.zeros_like(x)                  #xと同じ次数の零行列をyの初期値とする
    for i in range(len(w)-1):
        y = y + w[i]*gauss(x,mu[i],v)   #y+=wiφi(x)
    y = y + w[len(w)-1]                 #y+=wM
    return y


#平均二乗誤差MSE (式(4))
def mse(y,t):
    return np.mean((y-t)**2)

#計画行列算出 (式(7))
def design_matrix(x,t,mu,v):
    n=x.shape[0]
    m=len(mu)
    phi=np.ones((n,m+1))            #計画行列、初期値は全て１にする(最後の１列は全て１になる)
    for j in range(m):
        phi[:,j] = gauss(x,mu[j],v) #計画行列のj列目を算出
    phi_T=np.transpose(phi)

    b=np.linalg.inv(phi_T.dot(phi)) #(φ*φ^-1)^-1
    c=b.dot(phi_T)                  #(φ^T*φ^-1)^-1*φ^T
    w=c.dot(t)                      #(φ^T*φ^-1)^-1*φ^T*t
    return w

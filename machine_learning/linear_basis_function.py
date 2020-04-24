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

import math
import matplotlib.pyplot as plt

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

#mを設定
M=[1,4,7,10,13,16]

plt.figure(figsize=(20,7.5))
plt.subplots_adjust(wspace=0.25,hspace=0.3)

for i in range(len(M)):
    #2*3のi+1番目にプロット
    plt.subplot(2,3,i+1)
    m=M[i]

    #ガウス関数の中心 はxの最小値〜最大値の間で設定
    mu=np.linspace(min(x),max(x),m)
    #w,y算出
    w=design_matrix(x,t,mu,1)
    y=linear_basis_func(w,x,mu,1)

    #入力値xを(yを対応づけたまま)ソート
    xy=[[x[i],y[i]] for i in range(len(x))]
    xy.sort(key=lambda a:a[0])
    xi,yi=zip(*xy)

    #標準偏差SD
    sd = math.sqrt(mse(y,t))

    #プロット
    plt.scatter(x,t,label='t')
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(t)-1,max(t)+1)

    plt.plot(xi,yi,'-',color='red',label='y')
    plt.legend(loc='lower right')
    plt.title("M={0:d}, SD={1:.2f}".format(m,sd))

    plt.grid(True)
plt.show()
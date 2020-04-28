import math
import matplotlib.pyplot as plt
import numpy as np
from linear_basis_function import mse
from linear_basis_function import design_matrix
from linear_basis_function import linear_basis_func

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

#mを設定
M=[1,5,9,13]

plt.figure(figsize=(20,7.5))
plt.subplots_adjust(wspace=0.25,hspace=0.3)

for i in range(len(M)):
    #2*2のi+1番目にプロット
    plt.subplot(2,2,i+1)
    m=M[i]

    #ガウス関数の中心 はxの最小値〜最大値の間で設定
    mu=np.linspace(min(x),max(x),m)
    #w,y算出
    w=design_matrix(x,t,mu,1)
    y=linear_basis_func(w,x,mu,1)

    #予測式を細かく表示させるためのデータ作成
    x_forplot = np.linspace(min(x),max(x),1000)
    y_forplot = linear_basis_func(w,x_forplot,mu,1)

    #標準偏差SD
    sd = math.sqrt(mse(y,t))

    #プロット
    plt.scatter(x,t,label='t')
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(t)-1,max(t)+1)

    plt.plot(x_forplot,y_forplot,'-',color='red',label='y')
    plt.legend(loc='lower right')
    plt.title("M={0:d}, SD={1:.2f}".format(m,sd))

    plt.grid(True)
plt.show()
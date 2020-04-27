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

#訓練データ,全体の3/4
n=(len(x)//4)*3
x_train=x[:n]
t_train=t[:n]

#テストデータ
x_test=x[n:]
t_test=t[n:]

#メイン(プロット)
plt.figure(figsize=(20,7.5))
plt.subplots_adjust(wspace=0.25,hspace=0.3)

for i in range(len(M)):
    plt.subplot(2,2,i+1)

    m=M[i]

    #ガウス関数の中心 はxの最小値〜最大値の間で設定
    mu=np.linspace(min(x_train),max(x_train),m)
    #訓練データでw,y算出
    w_train = design_matrix(x_train,t_train,mu,1)
    y_test = linear_basis_func(w_train,x_test,mu,1)
    y_train = linear_basis_func(w_train,x_train,mu,1)

    #入力値xを(yを対応づけたまま)ソート
    xy_test=[[x_test[i],y_test[i]] for i in range(len(x_test))]
    xy_test.sort(key=lambda a:a[0])
    xi_test,yi_test=zip(*xy_test)

    xy_train=[[x_train[i],y_train[i]] for i in range(len(x_train))]
    xy_train.sort(key=lambda a:a[0])
    xi_train,yi_train=zip(*xy_train)

    #標準偏差SD
    sd = math.sqrt(mse(y_test,t_test))

    #プロット
    plt.scatter(x_train,t_train,c='white',label='train',edgecolors="black")
    plt.scatter(x_test,t_test,c='green',label='test')
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(t)-1,max(t)+1)

    plt.plot(xi_test,yi_test,'-',color='red',label='y_test')
    plt.plot(xi_train,yi_train,'-',alpha=0.5,color='blue',label='y_train')
    plt.legend(loc='lower right')
    plt.title("M={0:d}, SD={1:.2f}".format(m,sd))

    plt.grid(True)
plt.show()
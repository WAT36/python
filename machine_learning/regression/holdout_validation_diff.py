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

#訓練データ,全体の3/4
n=(len(x)//4)*3
x_train=x[:n]
t_train=t[:n]

#テストデータ
x_test=x[n:]
t_test=t[n:]

#M毎の標準偏差SD
sd_train=[]
sd_test=[]

#メイン(プロット)
plt.figure(figsize=(10,7.5))

M=[i for i in range(1,14)]

for m in M:

    #ガウス関数の中心 はxの最小値〜最大値の間で設定
    mu=np.linspace(min(x_train),max(x_train),m)
    #訓練データでw,y算出
    w_train = design_matrix(x_train,t_train,mu,1)
    y_test = linear_basis_func(w_train,x_test,mu,1)
    y_train = linear_basis_func(w_train,x_train,mu,1)

    #標準偏差SD算出
    sd_train.append(math.sqrt(mse(y_train,t_train)))
    sd_test.append(math.sqrt(mse(y_test,t_test)))

#プロット
plt.xlim(min(M)-1,max(M)+1)
plt.ylim(min(min(sd_train),min(sd_test))-1,max(max(sd_train),max(sd_test))+1)

plt.plot(M,sd_train,'-',color='blue',label='SD_train')
plt.plot(M,sd_test,'-',color='red',label='SD_test')
plt.legend(loc='upper left')

plt.grid(True)
plt.show()
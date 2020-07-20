from k_means import calc_r
import matplotlib.pyplot as plt
import numpy as np

#入力値
x = np.load('x.npy')

#クラスタの中心位置
mu=np.array([[38,6],[40,6],[42,6]])

#クラスタ計算
mu,r = calc_r(x,mu)

#プロット
color=['red','blue','green']

#各入力データをクラスタリング結果(色分け)とともに表示
for i in range(len(mu)):
    plt.plot(x[r[:,i]==1,0],x[r[:,i]==1,1],linestyle='none',markeredgecolor='black',marker='o',color=color[i])

#各クラスタの中心位置を表示(★型)
for i in range(len(mu)):
    plt.plot(mu[i,0],mu[i,1],linestyle='none',markeredgecolor='black',marker='*',color=color[i])

plt.xlim([min(x[:,0])-1,max(x[:,0])+1])
plt.ylim([min(x[:,1])-1,max(x[:,1])+1])

plt.xlabel('temperature[℃]')
plt.ylabel('pH')

plt.grid(True)
plt.show()
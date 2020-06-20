#入力データを２次元座標にプロットする
from plot_2d_2class import plot_data_2d
import matplotlib.pyplot as plt
import numpy as np

#入力値
x = np.load('x_2d2class.npy')
#目標値
t = np.load('t_2d2class.npy')

plot_data_2d(x,t)

plt.xlim([min(x[:,0])-1,max(x[:,0])+1])
plt.ylim([min(x[:,1])-1,max(x[:,1])+1])

plt.xlabel('temperature[℃]')
plt.ylabel('pH')

plt.legend(loc='best')
plt.grid(True)
plt.show()

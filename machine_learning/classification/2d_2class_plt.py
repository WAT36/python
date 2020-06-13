import numpy as np
import matplotlib.pyplot as plt

#入力値
x = np.load('x_2d2class.npy')
#目標値
t = np.load('t_2d2class.npy')

print(x)
print(t)
color=['black','white']
lab=['0:bad','1:good']
for i in range(2):
    plt.plot(x[t[:]==i,0],x[t[:]==i,1],
    linestyle='none',markeredgecolor='black',marker='o',color=color[t[i]],alpha=0.8,label=lab[i])
#    plt.plot(x[i][0],x[i][1],linestyle='none',markeredgecolor='black',marker='o',color=color[t[i]],alpha=0.8,label=lab[t[i]])
plt.grid(True)

plt.xlim([36,43])
plt.ylim([4,7.5])

plt.xlabel('temperature[℃]')
plt.ylabel('pH')

plt.legend(loc='best')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cross_entropy_error import ave_cross_entropy_error

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

#解像度
min_x=-0.5
max_x=0.5
n=100
w_range=np.array([[min_x,max_x],[min_x,max_x]])
x0=np.linspace(w_range[0,0],w_range[0,1],n)
x1=np.linspace(w_range[1,0],w_range[1,1],n)
xx0,xx1 = np.meshgrid(x0,x1)
g=np.zeros((len(x1),len(x0)))


w=np.zeros(2)
for i0 in range(n):
    for i1 in range(n):
        w[0]=x0[i0]
        w[1]=x1[i1]
        g[i1,i0] = ave_cross_entropy_error(w,x,t)
#        print(i0,i1,w[0],w[1],g[i1,i0])


#可視化
plt.figure(figsize=(10,5))
ax = plt.subplot(1,2,1,projection='3d')
plt.subplots_adjust(wspace=0.5)
ax.plot_surface(xx0,xx1,g,color='blue',edgecolor='black',rstride=10,cstride=10,alpha=0.4)
ax.set_xlabel('$w_0$',fontsize=14)
ax.set_ylabel('$w_1$',fontsize=14)
ax.set_xlim(min_x,max_x)
ax.set_ylim(min_x,max_x)
ax.set_zlim(0,10)

plt.subplot(1,2,2)
cont = plt.contour(xx0,xx1,g,20,colors='black',levels=[0.25,0.5,1,1.5,2])
cont.clabel(fmt='%1.1f',fontsize=8)
plt.xlabel('$w_0$',fontsize=14)
plt.ylabel('$w_1$',fontsize=14)
plt.xlim(min_x,max_x)

plt.grid(True)
plt.show()
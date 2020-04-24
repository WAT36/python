import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x0 = np.array([117.9,164.3,171.6,172.7,132.8,170.2,152.3,163.8,168.8,127.2,142.3,156.4,173.1,176.9,158.4,127.1,147.4,123.7,152.0,174.1])
x1 = np.array([28.0,58.2,60.1,65.2,35.0,60.9,51.9,56.4,62.9,27.0,44.9,45.9,68.0,67.9,59.1,30.8,45.6,36.1,39.9,69.5])
t = np.array([6,16,19,18,9,16,12,14,15,7,10,12,17,18,15,8,11,7,11,19])

x01,x10=np.meshgrid(x0,x1)

fig=plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("height")
ax.set_ylabel("weight")
ax.set_zlabel("old")

ax.plot(x0,x1,t,marker="o",linestyle='None')

###

cov_tx0 = np.mean(t*x0) - np.mean(t)*np.mean(x0)
cov_tx1 = np.mean(t*x1) - np.mean(t)*np.mean(x1)
cov_x0x1 = np.mean(x0*x1) - np.mean(x0)*np.mean(x1)
w0 = (cov_tx1*cov_x0x1 - np.var(x1)*cov_tx0)/(cov_x0x1*cov_x0x1 - np.var(x0)*np.var(x1))
w1 = (cov_tx0*cov_x0x1 - np.var(x0)*cov_tx1)/(cov_x0x1*cov_x0x1 - np.var(x0)*np.var(x1))
w2 = -1 * w0 * np.mean(x0) - w1 * np.mean(x1) + np.mean(t)

print("w0:{0}".format(w0))
print("w1:{0}".format(w1))
print("w2:{0}".format(w2))

def plane(x0,x1):
    return w0*x0 + w1*x1 + w2


h = np.linspace(110,180,71)
w = np.linspace(25,75,71)

old=np.zeros((len(w),len(h)))

for hi in range(len(h)):
     for wi in range(len(w)):
             old[wi,hi] = plane(h[hi],w[wi])

hh,ww = np.meshgrid(h,w)

ax.plot_surface(hh,ww,old,rstride=1,cstride=1,alpha=0.3,color='red',edgecolor='black')

plt.show()

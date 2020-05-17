import numpy as np
import matplotlib.pyplot as plt

x=[35.9,42.3,36.6,40.0,42.1,37.8,38.9,41.1,39.2,40.2,43.3,39.3,37.2,39.5,40.4,41.5,35.1,44.1,43.7,39.4]
t=[0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0]

#x,tをnpyファイルに保存
np.save('x.npy',x)
np.save('t.npy',t)

fig, ax = plt.subplots(facecolor="w")
ax.scatter(x,t)

ax.set_xticks(np.arange(35,45,1))
ax.set_yticks([0,1])
ax.grid(True,linestyle=':')

plt.xlabel('x')
plt.ylabel('t')

plt.show()
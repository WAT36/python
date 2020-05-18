import numpy as np
import matplotlib.pyplot as plt

#入力値
x = np.load('x.npy')
#目標値
t = np.load('t.npy')

#直線モデル作成
##t*x
tx = [t[i]*x[i] for i in range(len(x))]
##x^2
xx = [x[i]*x[i] for i in range(len(x))]
##w0
w0 = (np.mean(tx) - np.mean(t)*np.mean(x))/(np.mean(xx) - np.mean(x)*np.mean(x))
##w1
w1 = np.mean(t) - w0*np.mean(x)

y1=np.array([min(x)-1,max(x)+1])
y2=(w0*y1)+w1

x_ans=[(0.5-w1)/w0 for _ in range(2)]
y_ans=[-0.1,1.1]


fig, ax = plt.subplots(facecolor="w")
ax.plot(y1,y2,color='black')
ax.plot(x_ans,y_ans,color='r',linestyle=':')
ax.scatter(x,t)

ax.set_xticks(np.arange(35,45,1))
ax.set_yticks([0,1])
ax.grid(True,linestyle=':')

plt.xlim(34,45)
plt.ylim(-0.1,1.1)

plt.xlabel('x')
plt.ylabel('t')

plt.show()
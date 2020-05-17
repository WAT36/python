import numpy as np
import matplotlib.pyplot as plt

x = np.load('x.npy')
t = np.load('t.npy')

def f(x):
    return (0.906006875 * x) - 92.445073277

y = f(x)

plt.scatter(x,t)

x=np.append(x,0)
y=np.append(y,f(0))
x=np.append(x,200)
y=np.append(y,f(200))

plt.plot(x,y,color='red')
plt.xlim(160,180)
plt.ylim(50,75)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

def L(p):
    return p*((1-p)**4)

x=np.linspace(0,1,100)
y=L(x)

plt.plot(x,y)
plt.grid(True)
plt.show()
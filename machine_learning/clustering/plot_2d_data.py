import numpy as np
import matplotlib.pyplot as plt
import numpy as np

#入力値
x = np.load('x.npy')

plt.plot(x[:,0],x[:,1],linestyle='none',markeredgecolor='black',marker='o',color='gray')

plt.xlim([min(x[:,0])-1,max(x[:,0])+1])
plt.ylim([min(x[:,1])-1,max(x[:,1])+1])

plt.xlabel('temperature[℃]')
plt.ylabel('pH')

plt.grid(True)
plt.show()

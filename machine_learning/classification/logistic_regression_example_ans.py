import numpy as np
import matplotlib.pyplot as plt
from sigmoid import sigmoid

w=[[1,0],[2,2],[-1,1]]
func_label=["x","2x+2","-x+1"]

#y=w0x+w1
def line_func(w,x):
    return w[0]*x + w[1]

plt.figure(figsize=(10,2.5))
plt.subplots_adjust(wspace=0.3)
for i in range(len(w)):
    
    plt.subplot(1,len(w),i+1)

    x=np.linspace(-10,10,1000)
    y=line_func(w[i],x)

    plt.plot(x,y,color='red')

    sig_y=sigmoid(y)
    plt.plot(x,sig_y,color='blue')

    ans_x=np.where(sig_y>0.5)
    if(np.min(ans_x)==0):
        ans_x=np.max(ans_x)
    else:
        ans_x=np.min(ans_x)
    print(ans_x)
    ans_x=[x[ans_x]]*2
    ans_y=[-2,3]
    plt.plot(ans_x,ans_y,color='black',linestyle='--')

    plt.xlim(-5,5)
    plt.ylim(-1,2)
    plt.grid(True)

plt.show()


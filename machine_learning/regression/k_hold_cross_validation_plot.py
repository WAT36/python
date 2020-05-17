import numpy as np
import matplotlib.pyplot as plt
from k_hold_cross_validation import k_hold_cross_validation

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

#分割数
k = len(x)
#m
M = range(1,10)

train=np.zeros(len(M))
test=np.zeros(len(M))

for i in range(len(M)):
    train_i,test_i=k_hold_cross_validation(x,t,M[i],k)
    train[i]=np.sqrt(np.mean(train_i))
    test[i]=np.sqrt(np.mean(test_i))


plt.xlim(min(M)-1,max(M)+1)
plt.ylim(min(min(train),min(test))-1,max(max(train),max(test))+1)

plt.plot(M,test,color='red',label='test')
plt.plot(M,train,color='blue',label='train')
plt.legend(loc='lower left')

plt.grid(True)
plt.show()

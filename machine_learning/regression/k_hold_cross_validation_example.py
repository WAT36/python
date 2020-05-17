import numpy as np
from k_hold_cross_validation import k_hold_cross_validation

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

mse_train,mse_test=k_hold_cross_validation(x,t,3,4)
print(mse_train)
print(mse_test)
#標準偏差(mseの平均の平方根)の算出
print("train:{0}".format(np.sqrt(np.mean(mse_train))))
print("test :{0}".format(np.sqrt(np.mean(mse_test))))

from fit_2d_2class import fit_2d_2class
import numpy as np

#入力値
x = np.load('x_2d2class.npy')
#実測値
t = np.load('t_2d2class.npy')

#wの初期値
w_init=[1,1,1]

#勾配法でwを求める
w=fit_2d_2class(w_init,x,t)

print("w0:{0}".format(w[0]))
print("w1:{0}".format(w[1]))
print("w2:{0}".format(w[2]))




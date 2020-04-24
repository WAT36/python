import numpy as np

def d_mse(w,x,t):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y-t)*x)
    d_w1 = 2 * np.mean(y-t)
    return d_w0,d_w1

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

#t*x
tx = [t[i]*x[i] for i in range(len(x))]
#x^2
xx = [x[i]*x[i] for i in range(len(x))]

#w0
w0 = (np.mean(tx) - np.mean(t)*np.mean(x))/(np.mean(xx) - np.mean(x)*np.mean(x))
#w1
w1 = np.mean(t) - w0*np.mean(x)

print("w0 = {0:.9f}".format(w0))
print("w1 = {0:.9f}".format(w1))

dJ=d_mse([w0,w1],x,t)
print("dJ(w0,w1) = [{0:.9f} {1:.9f}]".format(dJ[0],dJ[1]))

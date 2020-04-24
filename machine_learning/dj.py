import numpy as np

def d_mse(w,x,t):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y-t)*x)
    d_w1 = 2 * np.mean(y-t)
    return d_w0,d_w1

def steepest_descent_method(x,t,a,n):
    w=[10,10]           #wの初期値
    alpha=a             #学習率
    N=n                 #繰り返し回数
    min_dJ=0.1          #勾配法をやめる勾配の絶対値の閾値
    w_i=np.zeros([N,2]) #w_i[j]にはj回の勾配法で算出したwの値が入る
    w_i[0,:]=w          #w_iの最初の1行をwにする
    for i in range(1,N):
        dJ=d_mse(w_i[i-1],x,t)
        w_i[i,0]=w_i[i-1,0]-alpha*dJ[0] #w0(t+1)=w0(t)-α*∂J/∂w0
        w_i[i,1]=w_i[i-1,1]-alpha*dJ[1] #w1(t+1)=w1(t)-α*∂J/∂w1
        if( max(np.absolute(dJ)) < min_dJ):
            break
    w0=w_i[i,0]     
    w1=w_i[i,1]     
    w_i=w_i[:i,:]   
    return w0,w1,dJ,w_i

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

w0,w1,dJ,w_history = steepest_descent_method(x,t,0.000034,10000000)
print("繰り返し回数:"+str(w_history.shape[0]))
print("w0:{0:.9f} ,w1:{1:.9f}".format(w0,w1))
print("dJ:"+str(dJ))


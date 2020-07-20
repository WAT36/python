import numpy as np

k=-1
x=[]
mu=[]
R=[]

#R計算
def calc_r(X,Mu):

    #初期化　入力データx、μとR用意
    x=np.array(X)
    mu=np.array(Mu)
    k=len(mu)
    R=np.zeros((len(x),k))

    for i in range(len(x)):
        ri=np.zeros(k)
        ri[0]=1
        R[i]=ri

    flag=True
    count=1

    while(flag):
        flag=False

        #Rを計算し更新
        for i in range(len(x)):
            d=[(x[i][0]-mu[j][0])**2 + (x[i][1]-mu[j][1])**2  for j in range(k)]
            ri=np.zeros(k)
            ri[d.index(min(d))]=1
            if(not np.allclose(R[i],ri)):
                flag=True
            R[i]=ri

        #μを調整
        for i in range(k):
            x_i=x[R[:,i]==1]
            mu_ix=np.mean(x_i[:,0])
            mu_iy=np.mean(x_i[:,1])
            mu[i]=np.array([mu_ix,mu_iy])
        
        count+=1
    
    return mu,R



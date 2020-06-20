from mpl_toolkits.mplot3d import axes3d
from logistic_regression_2d import logistic_regression_2d
from logistic_regression_2d import logistic2d_for_plot
from fit_2d_2class import fit_2d_2class
import numpy as np
import matplotlib.pyplot as plt

#w,xを入力したときに３次元グラフ表示

#入力値
x = np.load('x_2d2class.npy')
#目標値
t = np.load('t_2d2class.npy')

#wの初期値
w_init=[1,1,1]
#パラメータwを求める
w=fit_2d_2class(w_init,x,t)

X_range0=[min(x[:,0])-1,max(x[:,0])+1]
X_range1=[min(x[:,1])-1,max(x[:,1])+1]


def show3d_logistic2(ax,w):
    xn=50
    x0=np.linspace(X_range0[0],X_range0[1],xn)
    x1=np.linspace(X_range1[0],X_range1[1],xn)
    xx0,xx1=np.meshgrid(x0,x1)
    y=logistic2d_for_plot(w,xx0,xx1)
    ax.set_xlabel("x0")
    ax.set_ylabel("x1")
    ax.set_zlabel("y")
    ax.plot_surface(xx0,xx1,y,color='blue',edgecolor='gray',rstride=5,cstride=5,alpha=0.3)


def show_data2_3d(ax,x,t):
    c=[[.5,.5,.5],[1,1,1]]
    for i in range(2):
        ax.plot(x[t[:]==i,0],x[t[:]==i,1],i,
        marker='o',color=c[i],markeredgecolor='black',
        linestyle='none',markersize=5,alpha=0.8)
    ax.view_init(elev=25,azim=-30)

#test
Ax = plt.subplot(1,1,1,projection='3d')
show3d_logistic2(Ax,w)
show_data2_3d(Ax,x,t)
plt.show()
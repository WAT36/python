from logistic_regression_2d import logistic_regression_2d
from logistic_regression_2d import logistic2d_for_plot
from fit_2d_2class import fit_2d_2class
from plot_2d_2class import plot_data_2d
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

def contour_logistic2(w):
    xn=30
    x0=np.linspace(X_range0[0],X_range0[1],xn)
    x1=np.linspace(X_range1[0],X_range1[1],xn)
    xx0,xx1=np.meshgrid(x0,x1)
    y=logistic2d_for_plot(w,xx0,xx1)
    cont=plt.contour(xx0,xx1,y,levels=(0.25,0.5,0.75),colors=['lightgray','red','lightgray'])
    cont.clabel(fmt="%1.2f",fontsize=10)

plt.figure(figsize=(7,7))

plot_data_2d(x,t)
contour_logistic2(w)

plt.grid(True)
plt.show()
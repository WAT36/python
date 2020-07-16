from logistic_regression_2d_3class import logistic_regression_2d_3class
from logistic_regression_2d_3class import cross_entropy_error_for_2d_3class
from logistic_regression_2d_3class import fit_2d_3class
from plot_2d_3class import plot_2d_3class
import matplotlib.pyplot as plt
import numpy as np

def contour_for_2d_3class(w,x):
    xn=30
    x0=np.linspace(min(x[:,0])-1,max(x[:,0])+1,xn)
    x1=np.linspace(min(x[:,1])-1,max(x[:,1])+1,xn)

    xx0,xx1=np.meshgrid(x0,x1)
    y=np.zeros((xn,xn,3))
    for i in range(xn):
        wk=logistic_regression_2d_3class(w,np.concatenate([xx0[:,i].reshape(xn,1),xx1[:,i].reshape(xn,1)],1))
        for j in range(3):
            y[:,i,j]=wk[:,j]
    for j in range(3):
        cont=plt.contour(xx0,xx1,y[:,:,j],levels=(0.5,0.999),colors=['red','white'])
        cont.clabel(fmt='%1.1f',fontsize=9)
    plt.grid(True)


#入力値
x = np.load('x_2d3class.npy')
#目標値
t = np.load('t_2d3class.npy')
#目標値をn*3行列にする
temp_t=t
t=np.zeros((t.shape[0],3))
for i in range(t.shape[0]):
    t[i,temp_t[i]]=1

w_init=np.zeros((3,3))

w=fit_2d_3class(w_init,x,t)

cee=cross_entropy_error_for_2d_3class(w,x,t)

print("CEE={0:.2f}".format(cee))

plt.figure(figsize=(7,7))
plot_2d_3class(x,temp_t)
contour_for_2d_3class(w,x)
plt.show()
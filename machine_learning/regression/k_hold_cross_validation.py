import numpy as np
from linear_basis_function import mse
from linear_basis_function import design_matrix
from linear_basis_function import linear_basis_func

#k分割交差検証 x:入力データ、t:実測値、m:線形基底関数モデルの数、k:分割する個数
def k_hold_cross_validation(x,t,m,k):
    x=np.array(x)
    t=np.array(t)
    n=x.shape[0]
    mse_train=np.zeros(k)
    mse_test=np.zeros(k)
    mu=np.linspace(min(x),max(x),m)
    for i in range(k):
        x_train = x[np.fmod(range(n),k) != i]
        t_train = t[np.fmod(range(n),k) != i]
        x_test = x[np.fmod(range(n),k) == i]
        t_test = t[np.fmod(range(n),k) == i]
        w_train = design_matrix(x_train,t_train,mu,1)

        y_train = linear_basis_func(w_train,x_train,mu,1)
        mse_train[i] = mse(y_train,t_train)

        y_test = linear_basis_func(w_train,x_test,mu,1)
        mse_test[i] = mse(y_test,t_test)

    return mse_train,mse_test


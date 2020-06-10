from cross_entropy_error import ave_cross_entropy_error
from scipy.optimize import minimize
from d_cee import d_cee
import numpy as np

def cee_solve(w_init,x,t):
    ans = minimize(ave_cross_entropy_error,w_init,args=(x,t),jac=d_cee,method="CG")
    return ans.x

w_init=[1,1]

#入力値
x = np.load('x.npy')
#実測値
t = np.load('t.npy')

w_ans=cee_solve(w_init,x,t)
print("w0:{0}".format(w_ans[0]))
print("w1:{0}".format(w_ans[1]))

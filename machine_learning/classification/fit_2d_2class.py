from cross_entropy_error_2d import ave_cross_entropy_error_2d
from scipy.optimize import minimize
from d_cee_2d import d_cee_2d
import numpy as np

#勾配法
def fit_2d_2class(w,x,t):
    result=minimize(ave_cross_entropy_error_2d,w,args=(x,t),jac=d_cee_2d,method="CG")
    return result.x
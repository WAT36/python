from logistic_regression import logistic_regression
from cross_entropy_error import ave_cross_entropy_error
from scipy.optimize import minimize
from d_cee import d_cee
import matplotlib.pyplot as plt
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

#データをプロット
#x,t
fig, ax = plt.subplots(facecolor="w")
ax.scatter(x,t)

ax.set_xticks(np.arange(35,45,1))
ax.set_yticks([0,0.5,1])
ax.grid(True,linestyle=':')

logi_x=np.linspace(30,50,1000)
logi_y=logistic_regression(w_ans,logi_x)
plt.plot(logi_x,logi_y,color='black')

#決定境界(y=0.5となる所を探す)
i=np.min(np.where(logi_y>0.5))
ans=(logi_x[i]+logi_x[i+1])/2
x_ans=[ans for _ in range(2)]
y_ans=[-0.2,1.2]
plt.plot(x_ans,y_ans,color='red',linestyle=':')
print("決定境界：x={0}".format(ans))

plt.xlim(34,45)
plt.ylim(-0.2,1.2)

plt.show()

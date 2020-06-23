import numpy as np
import matplotlib.pyplot as plt

def plot_2d_3class(x,t):
    color=['black','gray','white']
    lab=['0:bad','1:so so','2:good']
    for i in range(len(lab)):
        plt.plot(x[t[:]==i,0],x[t[:]==i,1],
        linestyle='none',markeredgecolor='black',marker='o',color=color[i],alpha=0.8,label=lab[i])

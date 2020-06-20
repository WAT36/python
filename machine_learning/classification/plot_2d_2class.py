import numpy as np
import matplotlib.pyplot as plt

def plot_data_2d(x,t):
    color=['black','white']
    lab=['0:bad','1:good']
    for i in range(2):
        plt.plot(x[t[:]==i,0],x[t[:]==i,1],
        linestyle='none',markeredgecolor='black',marker='o',color=color[i],alpha=0.8,label=lab[i])

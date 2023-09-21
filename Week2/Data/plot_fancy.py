import numpy as np
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.figure(figsize=(7,6),dpi=600)
font = {'family' : 'Microsoft YaHei','weight' : 'bold','size' : 20}
font1 = {'family' : 'Microsoft YaHei','weight' : 'bold','size' : 30}
plt.rcParams["axes.linewidth"] = 3.0
plt.rcParams["axes.labelsize"] = 28
plt.rcParams["axes.titlepad"] = 1
plt.suptitle('Conf. 2 at 300 K',size=28,weight='semibold',y=0.97)
xlimrange0=0
xlimrange1=50000
ylimrange0=100
ylimrange1=200
xtickrange= np.arange(0,50000,1000)
ytickrange= np.arange(100,200,10)
a1=plt.subplot(1,1,1)
qdme = pd.read_csv('/home/rr4398/comp-lab-class/comp-lab-class-2023/Week2/Data/plot1.txt')
qdme.columns=["t","e1","e2","e3","e4","e5","e6"]
t = qdme["t"]
TCF_e1 = qdme["e1"]
TCF_e2 = qdme["e2"]
TCF_e3 = qdme["e3"]
TCF_e4 = qdme["e4"]
TCF_e5 = qdme["e5"]
TCF_e6 = qdme["e6"]

plt.plot(t,TCF_e1, color = 'blue',linewidth=2.0, linestyle= '-',label ='energy6',ms=10)

plt.legend(frameon=False,loc="upper center",prop=font)

#plt.yticks(fontproperties = 'Microsoft YaHei',weight='bold')
#plt.xticks(xtickrange,fontproperties = 'Microsoft YaHei',weight='bold')
#plt.xlim(xlimrange0,xlimrange1)
#plt.ylim(ylimrange0,ylimrange1)
#plt.yscale('log')
#plt.tick_params(direction='in',labelsize=24, length=10, width=3,top=True,right=True)
plt.xlabel(r'Time',font1)
plt.ylabel(r'Potential Energy')
plt.subplots_adjust(wspace=0,hspace=0,left=0.15)
plt.savefig('potential.pdf', dpi=500, bbox_inches='tight',facecolor='white')

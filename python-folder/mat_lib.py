import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# plt.plot([1,2,3],[4,5,6],label='line',color='r',linewidth='2',marker='.',markersize=12,markeredgecolor='b',linestyle='--')
# #short form
plt.figure(figsize=(5,3),dpi=200)
plt.plot([1,2,3],[2,4,6],'r.--',label='2x')
x=np.arange(0,4.5,0.5)
plt.plot(x[:5],x[:5]**2,label='graph2',marker='^')
plt.plot(x[4:],x[4:]**2,'b*--',label='graph3')
plt.title('graph',fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel("x axis")
plt.ylabel("y axis")
# xticks-change the numbers on axis
# plt.xticks([2,4,6])
plt.legend()#shows label
#re size graph



plt.show()
#bar chart
labels=('A','B')
value=(1,2)
var=plt.bar(labels,value)
var[0].set_hatch('/')
plt.show() 

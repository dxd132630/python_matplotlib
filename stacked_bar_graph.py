# Author      : Deeti Deshpande
# File name   : stacked_bar_graph.py
# Description : Stacked bar graph plotting 

import numpy as np
import matplotlib.pyplot as plot

#Finds the aggregate of the list items
def aggSum(*listItem):
    return [sum(values) for values in zip(*listItem)]

#data points of y-axis
N = 5
A = (3,10,21,2,6)
B = (8,5,5,0.5,2)
C = (12,17,0.5,22,5)
D = (15.5,6,5,12,4)
E = (1,11,2,16,6)

# data point for x-axis
x = np.arange(N)   


width = 0.30
plot.grid()

p1 = plot.bar(x+width,A,width,color='b',label='A')
p2 = plot.bar(x+width,B,width,color='b',alpha=0.5,bottom=aggSum(A),label='B')
p3 = plot.bar(x+width,C,width,color='k',alpha=0.3,bottom=aggSum(A,B),label='C')
p4 = plot.bar(x+width,D,width,color='r',alpha=0.5,bottom=aggSum(A,B,C),label='D')
p5 = plot.bar(x+width,E,width,color='r',alpha=0.9,bottom=aggSum(A,B,C,D),label='E')

plot.title('user activity')
plot.yticks(np.arange(0,70,10))
plot.xticks(width+(x+width/2), ('M', 'T', 'W', 'Th', 'F') )
plot.legend()

plot.show()

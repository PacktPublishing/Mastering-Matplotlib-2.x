import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.widgets import RectangleSelector
ax1 = plt.subplot(111)
xpts = np.random.rand(100) 
ypts = np.random.rand(100) 
s = 10*np.ones(100)
points = ax1.scatter(xpts, ypts, s=s, c='b')
ax1.set_xlim(0,1)
ax1.set_ylim(0,1)
def changepoints(e1, e2):
    sizes = points.get_sizes()
    x0, x1 = sorted([e1.xdata, e2.xdata])
    y0, y1 = sorted([e1.ydata, e2.ydata])
    sizes[np.where((xpts > x0) & (xpts < x1) & (ypts > y0) & (ypts < y1))] = 50
    points.set_sizes(sizes)
    plt.gcf().canvas.draw()
    
rect = RectangleSelector(ax1, onselect=changepoints)
plt.show()

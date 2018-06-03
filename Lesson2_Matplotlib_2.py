#from mpl_toolkits.mplot3d import Axes3D, get_test_data
import matplotlib.pyplot as plt
from numpy import arange

''' fig = plt.figure()
ax = fig.add_subplot(111, projection='3D')

x,y,z = axes3D.get_test_data(0.05)
ax.plot_wireframe(x,y,z,rstride=10,cstride=10)
plt.pause(4) '''
#plt.show()

from numpy import arange, sin
a = arange(0,20,0.3)
b = sin(a)

ll = plt.plot(a,b)
plt.pause(4)
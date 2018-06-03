from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x,y,z = axes3d.get_test_data(0.05)
ax.plot_wireframe(x,y,z,rstride=10,cstride=10)
plt.pause(4)
#plt.show()

a = arange(0,20,0.3)
b = sin(a)

ll = plt.plot(a,b)
plt.pause(4)

# coding: utf-8

# In[7]:


import pylab as plb
k = 8
x = plb.arange(k)
y1 = plb.rand(k) * (1 - x/k)
y2 = plb.rand(k) * (1 - x/k)
plb.axes([0.075, 0.075, 0.88, 0.88])

plb.bar(x, +y1, facecolor = '#9922aa', edgecolor = 'green')
plb.bar(x, -y2, facecolor = '#ff3366', edgecolor = 'green')

for a, b in zip(x, y1):
    plb.text(a+0.41, b+0.08, '%.3f' %b, ha = 'center', va='bottom')
for a, b in zip(x, y2):
    plb.text(a+0.41, b-0.08, '%.3f' %b, ha = 'center', va='bottom')

plb.xlim(-0.5, k), plb.ylim(-1.12, +1.12)
plb.grid(True)
plb.show()


# In[10]:


# Animate the graph above. Jupyter does not animate
import pylab as plb
k = 8
x = plb.arange(k)

i = 0
for i in range(5):
    y1 = plb.rand(k) * (1 - x/k)
    y2 = plb.rand(k) * (1 - x/k)
    plb.axes([0.075, 0.075, 0.88, 0.88])

    plb.bar(x, +y1, facecolor = '#9922aa', edgecolor = 'green')
    plb.bar(x, -y2, facecolor = '#ff3366', edgecolor = 'green')

    for a, b in zip(x, y1):
        plb.text(a+0.21, b+0.08, '%.3f' %b, ha = 'center', va='bottom')
    for a, b in zip(x, y2):
        plb.text(a+0.21, b-0.08, '%.3f' %b, ha = 'center', va='bottom')

    plb.xlim(-0.5, k), plb.ylim(-1.12, +1.12)
    plb.grid(True)
    plb.pause(1)
    plb.cla()
    
    i += 1


# In[13]:


# Scatter plot
import pylab as plb

x = plb.rand(1,2, 1500)
y = plb.rand(1,2,1500)

plb.axes([0.075, 0.075, 0.88, 0.88])
plb.cla()

plb.scatter(x, y, s=65, alpha=0.75, linewidth=0.125, c=plb.arctan2(x, y))

plb.grid(True)
plb.xlim(-0.085, 1.085), plb.ylim(-0.085, 1.085)
plb.pause(1)


# In[16]:


#plb.cla()
array = plb.random((80, 120))
plb.imshow(array, cmap = plb.cm.gist_rainbow_r)
plb.pause(1)


# In[21]:


import matplotlib.image as img
import matplotlib.pyplot as plt

image = img.imread('minimal-desktop-wallpaper-at-home.png')
plt.imshow(image)
plt.pause(1)

luminosity = image[:,:,0]
plt.imshow(luminosity)

plt.show(5)

plt.imshow(luminosity, cmap = 'hot')
plt.show(5)
plt.imshow(luminosity, cmap = 'spectral')
plt.show(5)


# In[22]:


plb.figure(1)
gaus_dist = plb.normal(-2, 2, size=512)#random vector

plb.hist(gaus_dist, normed=True, bins=24)
plb.title("Gaussian Distribution / Histogram")

plb.xlabel("Value")
plb.ylabel("Frequency")
plb.grid(True)
plb.show()


# In[24]:



#Histogram 2
plb.figure(2)
gaus_dist = plb.normal(size=512)
unif_dist = plb.uniform(-5,5, size=512) # uniform distibution vector

plb.hist(unif_dist, bins=24, histtype='stepfilled', normed=True, color='cyan', label='uniform')

plb.hist(gaus_dist, bins=24, histtype='stepfilled', normed=True, color ='orange', label='Gaussian', alpha=0.65)

plb.legend(loc = 'upper left')
plb.title("Gaussian vs Uniform Distribution / Histogram")
plb.xlabel("Value")
plb.ylabel("Frequency")
plb.grid(True)
plb.show()


# In[34]:


plb.figure('How do we get to work?')
plb.axes([0.035, 0.035, 1.09, 1.9])

l = 'Car', 'Truck', 'Boat', 'Dingie', 'Train', 'Plane', 'Bus', 'Rocket', 'Train', 'Other'
b = plb.round_(plb.random(10), decimals =2)
c = ['blue', 'red', 'green', 'gray', 'yellowgreen', 'gold', 'lightskyblue','lightcoral', 'cyan', 'orange']

e = (0,0,0,0,0,0,0.2, 0, 0, 0)

plb.cla()
plb.pie(b, explode=e, labels=l, colors = c, radius = 0.75, autopct='%1.2f%%', shadow=True, startangle=25)

plb.axis('equal')
plb.xticks(())
plb.yticks(())

plb.show()


# In[38]:


#Contour plot
def f(x,y):
    return (2-x/3 + x**6 + 2.125*y) * plb.exp(-x**2 -y**2)

n = 128
x = plb.linspace(-2,2, n)
y = plb.linspace(-1,1, n)

A,B = plb.meshgrid(x, y)

plb.cla()
plb.axes([0.075, 0.075, 0.92, 0.92])

plb.contourf(A, B, f(A, B), 12, alpha=0.50,cmap=plb.cm.gist_rainbow)

C = plb.contour(A, B, f(A, B), 8, colors='black', linewidths=0.65)

plb.clabel(C, inline=1, fontsize=14)
plb.xticks(())
plb.yticks(())
plb.show()


# In[45]:


plb.axes([0.065, 0.065, 0.88, 0.88], polar = True)

Q = 24
t = plb.arange(0.015, 3*plb.pi, 3*plb.pi / Q)
rad = 12 * plb.rand(Q)
w = plb.pi / 4 * plb.rand(Q)

ba = plb.bar(t, rad, width= w)

for r, bar in zip(rad, ba):
    bar.set_facecolor(plb.cm.jet(r/12))
    bar.set_alpha(0.75)

plb.show()


# In[49]:


from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(plb.figure())
x = plb.arange(-6, 3, 0.35)
y = plb.arange(-6, 6, 0.35)

x, y = plb.meshgrid(x,y)
k = plb.sqrt(x**2 + y**2)
z = plb.sin(k)

ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap = plb.cm.gist_ncar)
ax.contourf(x, y, z, zdir = 'z', offset=-3, cmap = plb.cm.gist_stern)
ax.set_zlim(-4, 4)

plb.show()


# In[ ]:


import collections
dict = {2:3, 1:89, 4:5, 3:0}
ord = 


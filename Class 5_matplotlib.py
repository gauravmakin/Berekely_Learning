
# coding: utf-8

# In[23]:


import numpy as np
f = np.matrix(np.ndarray(shape=(3,3), dtype=complex))
type(f)


# In[24]:


np.random.rand(3,2)


# In[25]:


np.random.randn(3,2)


# In[32]:


np.random.random(3)


# In[33]:


np.random.randint(30,45)


# MATPLOTLIB

# In[37]:


import pylab as plb
plb.array([[2,3,4],[5,6,7]])


# In[44]:


import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-np.pi*2, np.pi*2, 512, endpoint = True)

b_sin, c_cos = np.sin(a), np.cos(a)

plt.plot(a, b_sin)
plt.plot(a, c_cos)
plt.show()


# In[45]:


# Can use the exact the same thing using pylab


# In[49]:


import pylab as plb
a = plb.linspace(-plb.pi*2, plb.pi*2, 512, endpoint = True)

b_sin, c_cos = plb.sin(a), plb.cos(a)

plb.plot(a, b_sin)
plb.plot(a, c_cos)

plb.figure(figsize = (10,16), dpi = 400)


# In[58]:


plb.subplot(3,2,5)
plb.subplot(3,2,2)


# In[64]:


plb.Line2D(a, b_sin, linewidth=2)
plb.subplot(3,2,5)
plb.plot(a, b_sin)
plb.show()


# In[69]:


plb.figure(figsize=(10,6), dpi = 120)
d = plb.linspace(-plb.pi*3, plb.pi*3, 128, endpoint=True)
d_sin = plb.sin(d)
d_cos = plb.cos(d)

plb.subplot(2,3,1)
plb.plot(d, d_sin, color='red', linewidth=1.5, linestyle= "-.")

plb.subplot(3,2,6)
plb.plot(d, d_cos, color='blue', linewidth=2.5, linestyle='--')


# In[78]:


plb.xlim(-8.0, 8.0)
plb.xticks(plb.linspace(-8, 8, 6, endpoint = True))

plb.ylim(-1.2, 1.4)
plb.yticks(plb.linspace(-1.2, 1.4, 4, endpoint = True))
plb.plot(d, d_cos, color='blue', linewidth=2.5, linestyle='--')

plb.savefig("lecture_5.png", dpi=175)
plb.show()


# In[90]:


plb.figure(figsize=(6,3), dpi=100)
e = plb.linspace(-plb.pi*2, plb.pi*2, 128, endpoint = True)
e_sin = plb.sin(e)
e_cos = plb.cos(e)

# subplot is allocating the location for the chart
# 2 rows, 1 column, use the 1st row
plb.subplot(2,1,1)

# ticks here lets to create the pi symbol
plb.xticks([-plb.pi*2,plb.pi,plb.pi*2],['$-2\pi$','$-\pi$','$2\pi$'])
#show legend
plb.plot(e, e_sin, color='blue', linewidth=2, linestyle='-.', label = 'sin')
plb.legend(loc='upper right')

# dynamic limiting of the axis
plb.xlim(e_sin.min()*6.5, e_sin.max()*6.5)
plb.ylim(e_sin.min()*1.2, e_sin.max()*1.2)

plb.subplot(2,1,2)
plb.plot(e, e_cos, color='red', linewidth=2, linestyle='--', label = 'cosine')
plb.legend(loc = 'lower right')
plb.xlim(e_cos.min()*6.5, e_cos.max()*6.5)
plb.ylim(e_cos.min()*1.2, e_cos.max()*1.2)

plb.title("Plot of sin and cos functions")


# In[89]:


plb.figure(figsize=(6,3), dpi=100)
f = plb.linspace(-plb.pi*2, plb.pi*2, 128, endpoint = True)
f_sin = plb.sin(f)
f_cos = plb.cos(f)

plb.subplot(2,1,1)
ax1 = plb.gca()
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')


# In[101]:


# Gaurav Makin
from numpy import matrix, array, random, min, max
import pylab as plb

my_ints = random.randint(0,11,600)
my_arr = random.randint(-3*plb.pi, 2*plb.pi, 500)


# In[110]:


def overwrite(my_arr):
    avg = (my_arr.min() + my_arr.max())/2
    
    for item in range(my_arr.size):
        if 2 < my_arr[item] < 9:
            continue
        else:
            my_arr[item] = avg
    return my_arr


# In[116]:


C = overwrite(my_ints)


# In[118]:


def normalized(a, axis=0, order=0.1):
    l2 = plb.atleast_1d(plb.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)


# In[119]:


D = normalized(C, 0, 0.1)
D


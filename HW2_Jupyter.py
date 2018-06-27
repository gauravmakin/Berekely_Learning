
# coding: utf-8

# In[32]:


import numpy as np

A = (np.random.random(15)).reshape(3,5)
A.shape


# In[33]:


A.size


# In[34]:


len(A)


# In[63]:


A = A[:3,:4]
A.shape


# In[85]:


B = A.T
B.shape


# In[50]:


np.min(B,0)[0]


# In[51]:


B.min()


# In[52]:


B.max()


# In[56]:


X = np.random.random(4)
X


# In[66]:


def multiply(myarray, mymatrix):
    result = myarray * mymatrix
    return result

D = multiply(X, A)
D


# In[72]:


#z = np.ndarray(shape = 1, dtype = complex)
z = np.sqrt([1+1j])
z


# In[73]:


z.real


# In[74]:


z.imag


# In[75]:


np.absolute(z)


# In[76]:


C = np.absolute(z) * D


# In[77]:


C


# In[86]:


B = str(B)
print(B)


# In[87]:


print('Pencho')


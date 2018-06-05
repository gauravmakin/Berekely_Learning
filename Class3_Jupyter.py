
# coding: utf-8

# CLASS 3 NOTES

# In[1]:


for k in ("Sarah", "Cars", "Python"):
    print("John likes %s" %k)


# In[4]:


def new_range(start, end, step):
    while start <= end:
        yield start    #yield is a generator preserving function local value
        start += step

for x in new_range(2,5,0.2):
    print(x)


# In[10]:


#Methods and functions are members of a Classes
class simple_class:
    """This Class is a just a functionality test"""
    a = 12
    def f():
        print("Hello World")

simple_class.__doc__


# In[11]:


simple_class.f()


# In[13]:


class method_1():
    def method_1a():
        print("Method 1a")
    def method_1b():
        print("Method 1b")

class class_test(method_1):
    def method_1a():
        print("Method 1a from class test")
    def method_2a():
        print("Stand alone method")


# In[15]:


class_test.method_1a()


# In[16]:


method_1.method_1a()


# In[17]:


# POLYMORPHISM EXAMPLE
class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow'
class Dog(Animal):
    def talk(self):
        return 'Woof Woof'


# In[21]:


import sys
sys.version_info


# In[22]:


sys.version


# In[28]:


public_var = 12
_private_var = 34

__all__ = ['public_var', '_private_var', '_private_func']

def public_func():
    sum_pub_priv = public_var + _private_var
    print("Public. The sum is {}".format(sum_pub_priv))

def _private_func():
    print('This is a private function')
    
class public_class:
    print("This is a public class")
class _private_class():
    print("This is a private class")


# In[32]:


#file = open('SampleTextFile_100kb.txt', 'r')
#sentences = file.readlines()
#print(sentences)
#file.close()


# In[31]:


# reset -f    #CLEARS THE MEMORY


# In[33]:


while True:
    try:
        a = int(input('Please enter a number: '))
        print('You entered number', a)
        print('I will now exit')
        break
    except ValueError:
        print('You entered an invalid number. Please try again')


# In[40]:


from numpy import arange
import time

N = int(input('Please enter a number: '))

x = arange(N)
y = range(N)

tic = time.clock()
x.sum()
toc = time.clock()
t_numpy = toc - tic

tic = time.clock()
sum(y)
toc = time.clock()
t_list = toc - tic

print("numpy: %.3e sec" %(t_numpy))
print("list: %.3e sec" %(t_list))
print("diff: %.3e sec" %(t_numpy-t_list))


# In[43]:


import numpy
c = numpy.arange(5, dtype=numpy.float16)


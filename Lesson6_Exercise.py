"""
1. Import pylab
2. Create a dic4onary with 5 keys and empty values in A
3. Using a func4on, assign random values to each key between [0:10], using a for loop
and return the result in B
4. Using a function, change the value of any member in B that is less than 5 with the
result from (4.1) (consider using an if statement in a loop):
    4.1 Using normal distribu4on with mean = 2 and std = 3 create an array of size 256 points
    4.2 Using a histogram with 12 bins, plot the result from 4.1 with a pause of 1 sec. Use
proper labeling (figure, 4tle, labels, legend, grid, etc.)

5. Assign the result from 4. in C
6. Update one of the keys in C with another using the pop feature
7. Update another key in C manually (add the new one and delete the old one)
8. Compare A, B and C using a short condi4onal expression
"""
import pylab as plb
#from numpy import random
#import collections

A = {'A':'','B':'','C':'','D':'','E':''}
print(A)

def my_func(my_dict):
    for i, j in my_dict.items():
        my_dict[i] = plb.randint(0,10)
    return my_dict

B = my_func(A)
print(B)

def replace(my_dict, my_array):
    for i, j in my_dict.items():
        if j < 5:
            my_dict[i] = my_array
        else:
            continue
    return my_dict


my_array = plb.normal(loc=2, scale=3, size=256)

C = replace(B, my_array)
C['A'] = C.pop('E')

#print(C)
C['F'] = 1980
del C['D']
#print(C)

# if A.values() < B.values():
#     print("A is less than B")
# elif A.values() < C.values():
#     print("A is less than C")
# else:
#     print('A is the father')
    

plb.figure(1)
<<<<<<< HEAD

plb.hist(my_array, density=True, bins=24)
plb.title("Histogram")

plb.xlabel("X-Axis")
plb.ylabel("Y-Axis")
plb.grid(True)
plb.pause(4)
=======

plb.hist(my_array, density=True, bins=24)
plb.title("Histogram")
>>>>>>> f261bbb916ab8ce246508f0d2b7e245ff1e83090

plb.xlabel("X-Axis")
plb.ylabel("Y-Axis")
plb.grid(True)
plb.pause(4)
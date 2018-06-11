# Name: Gaurav Makin                                    #1

import numpy as np

# 2. Create matrix
A = np.matrix(np.random.random((3,5)))
#print(A)

# 3. Size and Lengh of Matrix A
#print("Size of matrix is:  ", A.size)
#print("Length of matrix is: ", len(A))
#print("Shape of matrix is :", np.shape(A))

# 4. 
A = A[:3,:4]
#print(A)

B = A.transpose()
#print("Transposed Matrix")
#print(B)

#print(B[:, :1].min())

#print(B.min())
#print(B.max())

X = np.random.random(size=4)
#print(type(X))
#print(X)

def multiply(my_vect, my_matr):
    D = np.dot(my_vect, np.array(my_matr.T))
    return D

#print("Multiplication of Vector and Matrix is: ", multiply(X, A))

my_comp = np.ndarray(shape = (2,3), dtype = complex, offset = np.float_().itemsize, order = 'C')
print(my_comp, "\n\n")

my_comp2 = np.ndarray(shape = (2,3), dtype = complex)
print(my_comp2)






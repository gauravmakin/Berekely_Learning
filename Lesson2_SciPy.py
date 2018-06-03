from scipy import poly1d

a = poly1d([4, 2, 6])
print("The Output is:\n")
print(type(a))
print(a)

print(a*a)

print(a.integ(k = 5))

print(a.deriv())

print(a([4, 5]))

# Fourier Transform and Inverse Fourier Transform
from scipy import fft, ifft
from numpy import array

print("\nFourier Transforms")

b = array([2.3, 3.1, 4.2, -1.8, 1.6, 5.9])
print(b)

c = fft(b)
print(c)

# Inverse. Should come back with b
print("\nInverse\n")
c_inverse = ifft(c)
print(c_inverse)

b_sum = b.sum()
print(b_sum)




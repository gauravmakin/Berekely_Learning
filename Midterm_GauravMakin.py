# NAME: Gaurav Makin
# COURSE: PYTHON FOR DATA ANALYTICS
# MIDTERM Jun 18, 2018

import pylab as plb
import numpy as np

# 1. Array of 12 consecutive odd numbers
A = np.arange(5,29,2)

# 2. Function calculating SMA using default window of 2
def sim_moving_avg(dataset, window=2):
    sma = np.convolve(dataset, np.ones((window,))/window, mode = 'valid')
    return sma

# 3. Function calculating CMA
def my_cma(dataset, cma):
    for i, x in enumerate(np.cumsum(dataset),1):
        cma.append(x/i)
    return cma

# 4. Function calls to get SMA
B = sim_moving_avg(A)
C = sim_moving_avg(A,4)

# Storing values
fxd_win_cma = []
my_cma(B,fxd_win_cma)
scnd_win_cma = []
my_cma(C, scnd_win_cma)

# 5. Printing output
print('The orginal array is: ', A)

print('\nCurrent window width: 2')
print('The SMA result is:\t', B)
print('The CMA result is:\t', fxd_win_cma)

print('\nCurrent window width: 4')
print('The SMA result is:\t', C)
print('The CMA result is:\t', scnd_win_cma)

# Plotting Figure
fig = plb.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(B, np.sin(B), color = 'red', lw=2, ls='-.', label = 'Sin(B)')
ax.plot(C, np.sin(C), color = 'blue', lw=3, ls='--', label = 'Sin(C)')
ax.set_title("Sin of B vs. Sin of C")
ax.grid(ls='-')
ax.legend(loc = 0)

plb.show()
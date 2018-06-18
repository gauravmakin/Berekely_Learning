# Moving Averages
import numpy as np
import pylab as plb
import matplotlib.pyplot as plt

a = np.random.randint(1,10,100)
print(a)

def moving_avg(dataset, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(dataset, weights, 'valid')
    return smas

def exp_moving_avg(dataset, window):
    weights = np.exp(np.linspace(-1.,0., window))
    weights /= weights.sum()

    expon = np.convolve(dataset, weights)[:len(dataset)]
    expon[:window]=a[window]
    return expon

b = moving_avg(a, 3)
c = exp_moving_avg(a, 3)

fig = plb.figure()
fig, axes = plb.subplots(nrows=2, ncols=1)
axes[0].plot(a,c,color='red', lw=3, ls='--', label='Scribble')
axes[0].set_title('Moving Average vs Exponential Average')
axes[1].plot(a,plb.sin(a))
plb.show()

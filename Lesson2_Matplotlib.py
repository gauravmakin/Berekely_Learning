from scipy.fftpack import fft
import numpy
import matplotlib.pyplot as plt

f = 600         # Sample Frequency
t = 1.0/f       # Period T
a = numpy.linspace(0.0,f*t,f)
b = numpy.sin(100.0 * 4.0)


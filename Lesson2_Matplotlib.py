from scipy.fftpack import fft
import numpy
import matplotlib.pyplot as plt

f = 600         # Sample Frequency
t = 1.0/f       # Period T
a = numpy.linspace(0.0, f*t, f)
b = numpy.sin(100.0 * 4.0*numpy.pi*a) + 0.6*numpy.sin(70.0*3.0*numpy.pi*a)
c = numpy.cos(50.0*2.0*numpy.pi*a)+0.8*numpy.sin(60.0*2.0*numpy.pi*a)

bf = fft(b)
cf = fft(c)

af = numpy.linspace(0.0, 1.0/(3.0*t), f/2)
plt.plot(af, 3.0/f * numpy.abs(bf[0:f/2]), 'r--')
plt.plot(af, 2.5/f*numpy.abs(cf[0:f/2]), 'b-')

plt.grid()
plt.pause(4)

plt.show()

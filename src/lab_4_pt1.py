import numpy as np
import matplotlib.pyplot as plt


amp = 1
fa = 8000
k = np.arange(0, 60)

#part A

fnot = 400
x_A = amp*np.sin(2*np.pi*k*fnot/fa)

plt.figure()
plt.stem(k, x_A)
plt.title("sinusoidal oscillation")
plt.xlabel("Sampling size index")
plt.ylabel("Amplitude")
plt.show()

#part B

fnot_2 = 960
x_B = amp*np.sin(2*np.pi*k*fnot_2/fa)

plt.figure()
plt.stem(k, x_B)
plt.title("sinusoidal oscillation part B")
plt.xlabel("Sampling size index")
plt.ylabel("Amplitude")
plt.show()



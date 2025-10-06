import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

fknot = 400
sampfreq = 8000
Time = 1 / sampfreq

# Time vectors
samples_400 = 400
samples_16000 = 16000
t_400 = np.arange(samples_400) * Time
t_16000 = np.arange(samples_16000) * Time

# Part a
x = np.cos(2 * np.pi * fknot * t_400)
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), d=Time)

plt.figure()
plt.title("DFT of Cosine Signal")
plt.plot(freqs[:samples_400 // 2], np.abs(X)[:samples_400 // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()


# Part b
def sawtooth_4harm(t, f0):
    omega0 = 2 * np.pi * f0
    return (2 / np.pi) * (np.sin(omega0 * t) - np.sin(2 * omega0 * t) / 2 +
                          np.sin(3 * omega0 * t) / 3 - np.sin(4 * omega0 * t) / 4)


saw_400 = sawtooth_4harm(t_400, fknot)  # 400 sample size
saw_16000 = sawtooth_4harm(t_16000, fknot)  # 16000 sample size

X_400 = np.fft.fft(saw_400)
X_16000 = np.fft.fft(saw_16000)
freqs_400 = np.fft.fftfreq(samples_400, d=Time)
freqs_16000 = np.fft.fftfreq(samples_16000, d=Time)

plt.figure()
plt.title("DFT of Sawtooth (400 samples)")
plt.plot(freqs_400[:samples_400 // 2], np.abs(X_400)[:samples_400 // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()

plt.figure()
plt.title("DFT of Sawtooth (16000 samples)")
plt.plot(freqs_16000[:samples_16000 // 2], np.abs(X_16000)[:samples_16000 // 2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()


# Part c
print("Frequency range for full info: 0 to", sampfreq / 2, "Hz")
print("Resolution (400 samples):", sampfreq / samples_400, "Hz")
print("Resolution (16000 samples):", sampfreq / samples_16000, "Hz")

# Part d:
t_square = np.arange(2000) * Time
square_wave = square(2 * np.pi * fknot * t_square)
X_square = np.fft.fft(square_wave)
freqs_square = np.fft.fftfreq(2000, d=Time)

plt.figure()
plt.title("DFT of Square Wave (2000 samples)")
plt.plot(freqs_square[:1000], np.abs(X_square[:1000]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
fnot = 960
amp = 2
T = 1/fnot   # time = 1/frequency
fA = 100000
t = np.linspace(0, 5*T, int(5*T*fA))

#part A
saw = amp*signal.sawtooth(2*np.pi*t*fnot)

#part b
phase_shift = -np.pi

saw_shifted = amp*signal.sawtooth(2*np.pi*t*fnot+phase_shift)


plt.figure()
plt.title("SAW")
plt.plot(t, saw, label = "original SAW")
plt.plot(t,saw_shifted, label = "phase shifted SAW")
plt.xlabel("Time(s)")
plt.ylabel("Amp")
plt.grid(True)
plt.legend()
plt.show()


#part c

plt.figure()
plt.plot(t, saw / amp, label='Original Sawtooth', linewidth=2)
for N in range(1, 6):
    saw_synth = np.zeros_like(t)

    for n in range(1, N + 1):
        coef = ((-1) ** (n + 1)) / n
        saw_synth += coef * np.sin(2 * np.pi * n * fnot * t)

    saw_synth = (2 / np.pi) * saw_synth

    plt.plot(t, saw_synth, label=f'{N} Harmonics')

plt.title('Sawtooth Synthesis with Fourier Series (1 to 5 Harmonics)')
plt.xlabel('Time (s)')
plt.ylabel('Amp (Normalized)')
plt.grid(True)
plt.legend()
plt.show()


#part d


t = np.linspace(0, 7*T, int(7*T*fA))


saw_original = amp * signal.sawtooth(2 * np.pi * fnot * t, 0.5)


time_shift = 0.0015
t_shifted = t + time_shift
saw_shifted = amp * signal.sawtooth(2 * np.pi * fnot * t_shifted, 0.5)


plt.figure()
plt.plot(t, saw_shifted, 'b--', label='Shifted Sawtooth Signal (t + 0.0015s)')

plt.title('Shifted and Unshifted Sawtooth Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amp')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


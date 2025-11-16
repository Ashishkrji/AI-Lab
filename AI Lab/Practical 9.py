#Python code for visualizing audio speech signal

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

# Read the speech WAV file
rate, data = wavfile.read("speech.wav")

# If stereo, convert to mono by taking the mean of the two channels
if len(data.shape) == 2:
    data = data.mean(axis=1)

# Create time axis in seconds
duration = data.shape[0] / rate
time = np.linspace(0., duration, data.shape[0])

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(time, data)
plt.title("Speech Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()


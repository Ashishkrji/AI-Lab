#Python code for Generating audio signals

import numpy as np
import sounddevice as sd

# Parameters
fs = 44100        # Sampling frequency (Hz)
duration = 2      # Duration of the signal (seconds)
f = 440           # Frequency of the sine wave (Hz) - A4 note

# Generate time axis
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate sine wave signal
signal = 0.5 * np.sin(2 * np.pi * f * t)  # Volume scaled to 0.5

# Play the sound
sd.play(signal, fs)
sd.wait()  # Wait until the sound has finished playing


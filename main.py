import requests
import numpy as np
import matplotlib.pyplot as plt

# URL to the .npy file
url = 'https://github.com/Duchstf/quench-detector/raw/signal-analysis/sample-data/Ramp27/ai0.npy'

# Download the .npy file
response = requests.get(url)
with open('ai0.npy', 'wb') as file:
    file.write(response.content)

# Load the .npy file
data = np.load('ai0.npy')

# Square the data to emphasize higher amplitudes
squared_data = data**2

# Compute the Fourier Transform of the squared data
fft_data = np.fft.fft(squared_data)
frequencies = np.fft.fftfreq(len(fft_data))

# Use slicing to plot every 100th sample
plt.figure(figsize=(10, 6))
plt.plot(frequencies[::100], np.abs(fft_data)[::100], color='pink')
plt.title('Frequency Spectrum of Squared Signal (Every 100th Sample)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

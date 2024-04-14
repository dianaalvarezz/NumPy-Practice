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

# Plot the data
plt.plot(data, color='pink')
plt.title('Plot of Data from ai0.npy')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

# Need to add array
array[:100]

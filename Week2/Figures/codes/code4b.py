import numpy as np
import matplotlib.pyplot as plt

# Define the file path
file_path = "data_vol.txt"

# Read data from the file
data = np.loadtxt(file_path)

# Split the data into x and y arrays
x = data[:, 0]
y = data[:, 1]

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Vol curve')

# Label the axes and add a title
plt.xlabel("Time (ns)")
plt.ylabel("Volume")
plt.title("Volume vs Time")

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig("vol_time.pdf")

plt.show()


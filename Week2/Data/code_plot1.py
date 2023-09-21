import numpy as np
import matplotlib.pyplot as plt

# Load data from the .txt file
data = np.genfromtxt("data.txt", skip_header=1, names=True)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each column of data except the first one (assuming it's "Time")
for i, column_name in enumerate(data.dtype.names):
    if i != 0:  # Skip the first column (assuming it's "Time")
        ax.plot(data[column_name], label=column_name)

# Set labels and title
ax.set_xlabel("Time")
ax.set_ylabel("Energies")
ax.set_title("Multiple Energies")

# Add a legend
ax.legend()

# Save the plot as a PDF
plt.savefig('plot.pdf')

# Show the plot (optional)
plt.show()







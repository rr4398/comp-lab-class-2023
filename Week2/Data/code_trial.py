import numpy as np
import matplotlib.pyplot as plt

# Load data from the .txt file
data = np.genfromtxt("data2.txt", skip_header=1, names=True)

# Specify the column you want to plot (e.g., "Temperature")
column_to_plot = "   K.E"

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the specified column with time
ax.plot(data["Time"], data[column_to_plot], label=column_to_plot)

# Set labels and title
ax.set_xlabel("Time")
ax.set_ylabel(column_to_plot)
ax.set_title(f"{column_to_plot} vs. Time")

# Add a legend
ax.legend()

# Save the plot as a PDF
plt.savefig(f'{column_to_plot}_plot.pdf')

# Show the plot (optional)
plt.show()

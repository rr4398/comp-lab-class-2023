import numpy as np
import matplotlib.pyplot as plt
import mdtraj as md
import os
os.chdir('/home/rr4398/comp-lab-class/comp-lab-class-2023/Week2/Analysis')
traj = md.load_xtc('/home/rr4398/comp-lab-class/comp-lab-class-2023/Week2/Data/1hz3_T310.stepid25000000.every100ps.nowater.xtc', top='/home/rr4398/comp-lab-class/comp-lab-class-2023/Week2/Data/1hz3_T310.start.nowater.gro')
# Calculate the end-to-end distance
end_to_end_distance = md.compute_distances(traj, [[0, traj.n_atoms - 1]])
# Calculate the radius of gyration
radius_of_gyration = md.compute_rg(traj)
time = np.arange(0, traj.n_frames) * traj.timestep

# Histogram for End-to-End Distance
plt.subplot(1, 2, 1)
plt.hist(end_to_end_distance, bins=20, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('End-to-End Distance (Angstroms)')
plt.ylabel('Density')
plt.title('Normalized Histogram of End-to-End Distance')

# Histogram for Radius of Gyration
plt.subplot(1, 2, 2)
plt.hist(radius_of_gyration, bins=20, density=True, alpha=0.7, color='green', edgecolor='black')
plt.xlabel('Radius of Gyration (Angstroms)')
plt.ylabel('Density')
plt.title('Normalized Histogram of Radius of Gyration')

# Adjust spacing between subplots
plt.tight_layout()

# Save the plot as a PDF
plt.savefig('../Figures/histograms.pdf')

# Show the plot (optional)
plt.show()

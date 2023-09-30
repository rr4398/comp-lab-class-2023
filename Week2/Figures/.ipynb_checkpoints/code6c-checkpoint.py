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
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# Plot end-to-end distance vs. time
plt.plot(time, end_to_end_distance, label='End-to-End Distance', marker='o', linestyle='-')
# Plot radius of gyration vs. time on the same y-axis
plt.plot(time, radius_of_gyration, label='Radius of Gyration', marker='x', linestyle='--')
# Label the axes and add a legend
plt.xlabel('Time (ps)')
plt.ylabel('Distance / Gyration Radius')
plt.legend()
# Add a title
plt.title('End-to-End Distance and Radius of Gyration vs. Time')
plt.subplots_adjust(wspace=0,hspace=0,left=0.15)
plt.savefig('../Figures/gyration_and_dist.pdf', dpi=500)
# Show the plot
plt.grid(True)
plt.show()

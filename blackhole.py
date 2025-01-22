import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Parameters for the black hole
event_horizon_radius = 0.1
accretion_disk_radius = 1.0
accretion_disk_thickness = 0.15

# Create event horizon (simple circle)
event_horizon = plt.Circle((0, 0), event_horizon_radius, color='black', lw=2)
ax.add_artist(event_horizon)

# Create accretion disk (simple ring shape)
theta = np.linspace(0, 2 * np.pi, 100)
x_disk = accretion_disk_radius * np.cos(theta)
y_disk = accretion_disk_radius * np.sin(theta)
accretion_disk = ax.fill(x_disk, y_disk, color='orange', alpha=0.7)

# Create a function for the accretion disk effect (rotation for animation)
def update(frame):
    # Clear the previous disk without removing the event horizon
    for artist in accretion_disk:
        artist.remove()

    # Simulate accretion disk rotation
    rotation_angle = np.radians(frame)
    x_disk_rot = accretion_disk_radius * np.cos(theta + rotation_angle)
    y_disk_rot = accretion_disk_radius * np.sin(theta + rotation_angle)
    
    # Redraw the rotating accretion disk
    accretion_disk_rot = ax.fill(x_disk_rot, y_disk_rot, color='orange', alpha=0.7)
    
    # Redraw the event horizon (should remain static)
    ax.add_artist(event_horizon)

    return accretion_disk_rot

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

plt.show()


# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

plt.show()


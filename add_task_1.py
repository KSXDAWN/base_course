import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


frames = 100  
interval = 100  


fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlim(-1, 7)
ax1.set_ylim(-1, 3)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)



R = 1  
t_max = 2 * np.pi  


cycloid_points_x = []
cycloid_points_y = []


line, = ax1.plot([], [], 'b-', linewidth=2)
point, = ax1.plot([], [], 'ro', markersize=8)
circle = plt.Circle((0, R), R, fill=False )
ax1.add_patch(circle)

def init1():
    line.set_data([], [])
    point.set_data([], [])
    return line, point


def animate1(i):
    
    t = t_max * i / frames
    
    
    x_center = R * t
    y_center = R
    
    
    x_point = R * (t - np.sin(t))
    y_point = R * (1 - np.cos(t))
    
    
    circle.center = (x_center, y_center)
    
    
    cycloid_points_x.append(x_point)
    cycloid_points_y.append(y_point)
    
    
    line.set_data(cycloid_points_x, cycloid_points_y)
    point.set_data([x_point], [y_point])
    
    
    ax1.plot([x_center, x_point], [y_center, y_point], 'r-', alpha=0.5)
    
    return line, point, circle


anim1 = FuncAnimation(fig1, animate1, init_func=init1,
                      frames=frames, interval=interval, blit=False)



plt.show()
 
anim1.save('animat.gif', writer="pillow")
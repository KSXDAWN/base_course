import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x0, y0 = 0, 0 

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.grid(True, alpha=0.3)

star_line, = ax.plot([], [], 'r-', lw=2)
center_point, = ax.plot([x0], [y0], 'bo', markersize=10, label='Центр')

def update(frame):
    alpha = frame * 0.02  
    t = np.linspace(0, 4*np.pi)
    
   
    x = 12*np.cos(t) + 8*np.cos(1.5*t)
    y = 12*np.sin(t) + 8*np.sin(1.5*t)
    
  
    X = x0 + x*np.cos(alpha) - y*np.sin(alpha)
    Y = y0 - x*np.sin(alpha) + y*np.cos(alpha)
    
    
    star_line.set_data(X, Y)
    
    return star_line, center_point


ani = FuncAnimation(fig, update, frames=314, interval=30, blit=True)
plt.show()
ani.save('animation_5.gif', writer="pillow")
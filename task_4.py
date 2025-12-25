import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33

x, y = [x0], [y0]

for n in range(1, 100, 1):
    x.append(x[n - 1]**2 - y[n - 1]**2 + C)
    y.append(2 * x[n - 1] * y[n - 1] + D)

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], [] 
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) 
ax.set_ylim(-1, 1) 

def update(frame):
    x.append(frame) 
    y.append(np.sin(frame)) 
    
    anim_object.set_data(x[:frame], y[:frame])

    return anim_object


ani = FuncAnimation(fig, 
                    update, 
                    frames=frames_interval,
                    interval=50) 

ani.save('animation_3.gif', writer="pillow")
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

N = 500
alpha = np.linspace(0, 2*np.pi, N)
x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

ball, = ax.plot(x, y, z, 'o', color='b') 
line, = ax.plot(x, y, z, '-', color='b') 

def animate(i):
    ball.set_data([x[i], y[i]])
    ball.set_3d_properties(z[i])
 
    line.set_data([x[:i], y[:i]])
    line.set_3d_properties(z[:i])

ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')
 
ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')
 
ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('Z')

ani = FuncAnimation(fig, animate, N, interval=50)
 
ani.save('3D_motion.gif')
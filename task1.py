import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
Theta, Phi = np.meshgrid(theta, phi)

phi_vals = np.linspace(0, 2, 50)
theta_vals = np.linspace(0, 2*np.pi, 50)
Phi_par, Theta_par = np.meshgrid(phi_vals, theta_vals)

X_1 = Phi_par * np.cos(Theta_par)
Y_1 = Phi_par * np.sin(Theta_par)
Z_1 = Phi_par**2

a, b, c = 1, 1, 1
X_2 = a * np.cos(Phi) * np.sinh(Theta)
Y_2 = b * np.sin(Phi) * np.sinh(Theta)
Z_2 = c * np.sin(Theta)

h = 0.5
phi_vals = np.linspace(0, 2, 50)
theta_vals = np.linspace(0, 4*np.pi, 50)
Phi_hel, Theta_hel = np.meshgrid(phi_vals, theta_vals)

X_3 = Phi_hel * np.cos(Theta_hel)
Y_3 = Phi_hel * np.sin(Theta_hel)
Z_3 = h * Theta_hel

l, m, n = 0.5, 0.5, 1
def f(theta):
    return np.sin(theta)

X_4 = Phi * np.cos(Theta) + l * f(Theta)
Y_4 = Phi * np.sin(Theta) + m * f(Theta)
Z_4 = n * f(Theta)

fig = plt.figure(figsize=(16, 12))

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X_1, Y_1, Z_1, alpha=0.8)
ax1.set_title('Параболоид')

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X_2, Y_2, Z_2, alpha=0.8)
ax2.set_title('Гиперболоид')

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X_3, Y_3, Z_3, alpha=0.8)
ax3.set_title('Геликоид')

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X_4, Y_4, Z_4, alpha=0.8)
ax4.set_title('Коноид')

plt.show()
plt.savefig('surface.png') 
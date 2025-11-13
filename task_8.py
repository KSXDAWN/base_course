import numpy as np
import task_7 as cnst

h = 100
a = np.radians(45)
b = np.radians(35)

v = np.sqrt((cnst.acceleration_of_gravity * h * np.tan(b)**2) / (2 * np.cos(a) ** 2 * (1 - np.tan(a) * np.tan(b))))
print('Значение V равно: ',v, 'м/c')

P = 3.14
T = 200
Q = 300
d = 2,71828


n = (2 * np.sqrt(P)) * np.sqrt(cnst.BOLTZMANN_CONSTANT) * (cnst.PLANCK_CONSTANT * T) ** (3/2) * (d ** (Q / cnst.BOLTZMANN_CONSTANT * T)) * Q ** (T / 2)
print('Значение N равно: ', n)

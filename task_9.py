import numpy as np
import task_7 as t1
x_0 = int(input('Введите значение x0: '))
y_0 = int(input('Введите значение y0: '))
V_x_0 = int(input('Введите значение Vx0: '))
V_y_0 = int(input('Введите значение Vy0: '))

A = np.zeros((6, 3))

for i in range(0, 6):
    x = x_0 + V_x_0 * i
    y = y_0 + V_y_0 * i - (t1.acceleration_of_gravity * (i ** 2) / 2)
    A[i, 0] = i
    A[i, 1] = x
    A[i, 2] = y
print(A)
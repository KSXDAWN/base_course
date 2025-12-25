import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры анимации
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Настройка осей
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.set_title('Движение точки по траектории')

ax2.set_xlim(0, 100)
ax2.set_ylim(-1.5, 1.5)
ax2.grid(True, alpha=0.3)
ax2.set_title('Графики координат')
ax2.set_xlabel('Время (кадры)')
ax2.set_ylabel('Значение')

# Инициализация объектов
point, = ax1.plot([], [], 'ro', markersize=10, label='Точка')
trajectory, = ax1.plot([], [], 'b-', alpha=0.5, linewidth=1, label='Траектория')
ax1.legend()

# Для второго графика (координаты во времени)
x_line, = ax2.plot([], [], 'r-', label='X(t)', alpha=0.7)
y_line, = ax2.plot([], [], 'b-', label='Y(t)', alpha=0.7)
ax2.legend()

# Массивы для хранения истории
x_history, y_history = [], []
time_history = []

# Параметры траектории (спиральная галактика)
def get_coordinates(frame):
    t = frame * 0.1
    # Сложная траектория
    r = 0.5 * t  # Радиус увеличивается со временем
    x = r * np.cos(2*t) * (1 + 0.3*np.sin(3*t))
    y = r * np.sin(2*t) * (1 + 0.3*np.cos(4*t))
    return x, y, t

def init():
    point.set_data([], [])
    trajectory.set_data([], [])
    x_line.set_data([], [])
    y_line.set_data([], [])
    return point, trajectory, x_line, y_line

def update(frame):
    # Получаем координаты для текущего кадра
    x, y, t = get_coordinates(frame)
    
    # Сохраняем историю
    x_history.append(x)
    y_history.append(y)
    time_history.append(frame)
    
    # Обновляем точку и траекторию
    point.set_data([x], [y])
    trajectory.set_data(x_history, y_history)
    
    # Обновляем графики координат
    x_line.set_data(time_history, x_history)
    y_line.set_data(time_history, y_history)
    
    # Ограничиваем историю последними 100 точками
    if len(x_history) > 100:
        x_history.pop(0)
        y_history.pop(0)
        time_history.pop(0)
    
    return point, trajectory, x_line, y_line

# Создание анимации (200 кадров, 50 мс между кадрами)
ani = FuncAnimation(fig, update, frames=200, 
                   init_func=init, interval=50, blit=True)

plt.tight_layout()
plt.show()
ani.save('animation_6.gif', writer="pillow")
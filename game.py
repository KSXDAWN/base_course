import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.patches import Polygon, Circle, Rectangle
from matplotlib.font_manager import FontProperties

# Настройка стиля и размера фигуры
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.set_aspect('equal')
ax.axis('off')

# Название анимации
plt.text(50, 55, 'Ракета летит на Киев', ha='center', va='center', 
         fontsize=16, fontweight='bold', color='darkred')

# Рисуем фон - небо и землю
sky = patches.Rectangle((0, 25), 100, 35, facecolor='lightblue', alpha=0.7)
ground = patches.Rectangle((0, 0), 100, 25, facecolor='#2E8B57', alpha=0.8)
ax.add_patch(sky)
ax.add_patch(ground)

# Рисуем упрощенную карту Украины и Киев
# Контур Украины (упрощенный)
ukraine_points = np.array([
    [15, 10], [20, 15], [25, 20], [30, 25], [35, 28], 
    [40, 30], [50, 32], [60, 30], [70, 25], [75, 20],
    [80, 15], [85, 10], [70, 8], [60, 10], [50, 12],
    [40, 10], [30, 8], [20, 6], [15, 10]
])

ukraine = patches.Polygon(ukraine_points, closed=True, 
                         facecolor='yellow', edgecolor='blue', 
                         linewidth=2, alpha=0.3)
ax.add_patch(ukraine)

# Киев - красная звезда
kiev_star = patches.RegularPolygon((50, 25), 5, radius=3, 
                                   facecolor='red', edgecolor='darkred', 
                                   linewidth=2, alpha=0.9)
ax.add_patch(kiev_star)
plt.text(50, 20, 'КИЕВ', ha='center', va='center', 
         fontsize=12, fontweight='bold', color='darkred')

# Облака для фона
clouds = []
for i in range(5):
    x = np.random.uniform(10, 90)
    y = np.random.uniform(30, 50)
    size = np.random.uniform(3, 6)
    cloud = patches.Circle((x, y), size, facecolor='white', alpha=0.6)
    ax.add_patch(cloud)
    clouds.append(cloud)

# Создаем ракету как группу патчей
rocket_body = patches.Rectangle((0, 0), 8, 2, facecolor='red', edgecolor='darkred', linewidth=2)
rocket_nose = patches.Polygon([[8, 0], [10, 1], [8, 2]], facecolor='darkred', edgecolor='black')
rocket_fins = [
    patches.Polygon([[0, 0], [-1, -1], [1, -1]], facecolor='darkred'),
    patches.Polygon([[0, 2], [-1, 3], [1, 3]], facecolor='darkred')
]
rocket_window = patches.Circle((4, 1), 0.5, facecolor='lightblue', edgecolor='darkblue')
rocket_flame = patches.Polygon([[-2, 0.5], [-4, 1], [-2, 1.5]], facecolor='orange', alpha=0.8)
rocket_inner_flame = patches.Polygon([[-2, 0.7], [-3, 1], [-2, 1.3]], facecolor='yellow', alpha=0.9)

# Добавляем все части ракеты на график
rocket_parts = [rocket_body, rocket_nose, rocket_window, rocket_flame, rocket_inner_flame] + rocket_fins
for part in rocket_parts:
    ax.add_patch(part)

# Начальная позиция ракеты
rocket_x = -10
rocket_y = 30

# Функция для обновления позиции ракеты
def update_rocket_position(x, y):
    for part in rocket_parts:
        if isinstance(part, patches.Rectangle):
            part.set_x(x)
            part.set_y(y)
        elif isinstance(part, patches.Polygon):
            # Обновляем координаты полигонов (нос, пламя, стабилизаторы)
            if part == rocket_nose:
                part.set_xy([[x + 8, y], [x + 10, y + 1], [x + 8, y + 2]])
            elif part == rocket_flame:
                part.set_xy([[x - 2, y + 0.5], [x - 4, y + 1], [x - 2, y + 1.5]])
            elif part == rocket_inner_flame:
                part.set_xy([[x - 2, y + 0.7], [x - 3, y + 1], [x - 2, y + 1.3]])
            elif part in rocket_fins:
                if rocket_fins.index(part) == 0:
                    part.set_xy([[x, y], [x - 1, y - 1], [x + 1, y - 1]])
                else:
                    part.set_xy([[x, y + 2], [x - 1, y + 3], [x + 1, y + 3]])
        elif isinstance(part, patches.Circle):
            part.center = (x + 4, y + 1)

# Функция анимации
def animate(frame):
    global rocket_x, rocket_y
    
    # Движение ракеты по траектории
    rocket_x += 0.8
    
    # Небольшие колебания по вертикали для реалистичности
    rocket_y = 30 + 2 * np.sin(frame * 0.1)
    
    # Обновляем позицию ракеты
    update_rocket_position(rocket_x, rocket_y)
    
    # Анимация пламени
    flame_size = 1.5 + 0.5 * np.sin(frame * 0.2)
    rocket_flame.set_xy([
        [rocket_x - 2, rocket_y + 1 - flame_size/2],
        [rocket_x - 4 * flame_size, rocket_y + 1],
        [rocket_x - 2, rocket_y + 1 + flame_size/2]
    ])
    
    rocket_inner_flame.set_xy([
        [rocket_x - 2, rocket_y + 1.3 - flame_size/3],
        [rocket_x - 3 * flame_size, rocket_y + 1],
        [rocket_x - 2, rocket_y + 0.7 + flame_size/3]
    ])
    
    # Добавляем след от ракеты
    if frame % 3 == 0:
        trail_size = np.random.uniform(0.1, 0.3)
        trail = patches.Circle((rocket_x - 3, rocket_y + 1), trail_size, 
                              facecolor='gray', alpha=0.3)
        ax.add_patch(trail)
    
    # Если ракета достигла Киева
    if rocket_x > 50 and rocket_x < 55:
        # Добавляем взрыв
        explosion = patches.Circle((50, 25), 2 + frame % 3, 
                                  facecolor='orange', alpha=0.7)
        ax.add_patch(explosion)
    
    # Если ракета улетела за пределы экрана
    if rocket_x > 110:
        rocket_x = -10
    
    return rocket_parts + clouds + [sky, ground, ukraine, kiev_star]

# Создаем анимацию
ani = animation.FuncAnimation(
    fig, animate, frames=200, 
    interval=50, blit=False, repeat=True
)

# Добавляем легенду траектории
trajectory_line, = ax.plot([], [], 'r--', alpha=0.5, linewidth=1)

def init_trajectory():
    trajectory_line.set_data([], [])
    return trajectory_line,

def update_trajectory(frame):
    if frame > 0:
        x_data = list(trajectory_line.get_xdata()) + [rocket_x + 4]
        y_data = list(trajectory_line.get_ydata()) + [rocket_y + 1]
        trajectory_line.set_data(x_data[-50:], y_data[-50:])
    return trajectory_line,

# Вторая анимация для траектории
ani_trajectory = animation.FuncAnimation(
    fig, update_trajectory, init_func=init_trajectory,
    frames=200, interval=50, blit=False, repeat=True
)

# Информационный текст
info_text = ax.text(10, 56, '', fontsize=10, color='darkblue')

def update_info(frame):
    global rocket_x
    distance_to_kiev = max(0, 50 - rocket_x)
    speed = 0.8 + 0.2 * np.sin(frame * 0.1)
    info_text.set_text(f'Дистанция до Киева: {distance_to_kiev:.1f} ед.\nСкорость: {speed:.1f} ед./кадр')
    return info_text,

# Третья анимация для информации
ani_info = animation.FuncAnimation(
    fig, update_info, frames=200, 
    interval=50, blit=False, repeat=True
)

plt.tight_layout()
plt.show()

ani.save('animation_5.gif', writer="pillow")



# Для сохранения анимации в файл (раскомментируйте если нужно)
# ani.save('rocket_to_kyiv.gif', writer='pillow', fps=20)
import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(x, y, length, angle, depth, ax):
    if depth == 0:
        return

    # Основний квадрат
    rect = plt.Rectangle((x, y), length, length, angle=angle, fill=True, color=np.random.rand(3,))
    ax.add_patch(rect)

    # Визначення нових координат та довжини для наступних квадратів
    new_length = length / np.sqrt(2)
    angle_rad = np.radians(angle)
    x0 = x + length * np.cos(angle_rad)
    y0 = y + length * np.sin(angle_rad)
    x1 = x0 + new_length * np.cos(angle_rad + np.pi / 4)
    y1 = y0 + new_length * np.sin(angle_rad + np.pi / 4)

    # Рекурсивний виклик для створення наступних рівнів дерева
    draw_pythagoras_tree(x0, y0, new_length, angle + 45, depth - 1, ax)
    draw_pythagoras_tree(x1, y1, new_length, angle - 45, depth - 1, ax)

def plot_pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Початкові параметри
    x, y, length, angle = 0, 0, 1, 0

    draw_pythagoras_tree(x, y, length, angle, depth, ax)

    plt.show()

# Задаємо рівень рекурсії (наприклад, 5)
plot_pythagoras_tree(5)

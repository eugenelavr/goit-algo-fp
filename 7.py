import random
import matplotlib.pyplot as plt

# Симуляція кидання двох кубиків
def roll_dice(num_rolls):
    counts = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильників для кожної можливої суми

    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1

    return counts

num_rolls = 100000
counts = roll_dice(num_rolls)

# Обчислення імовірностей
probabilities = {sum_val: count / num_rolls for sum_val, count in counts.items()}

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='blue')
plt.xlabel('Сума')
plt.ylabel('Імовірність')
plt.title('Імовірність суми двох кубиків за методом Монте-Карло')
plt.grid(True)
plt.show()

probabilities

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорійності до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if details['cost'] <= budget:
            chosen_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Ініціалізація таблиці динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.items())
    
    for i in range(1, len(item_list) + 1):
        for w in range(1, budget + 1):
            item_name, item_details = item_list[i-1]
            if item_details['cost'] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-item_details['cost']] + item_details['calories'])
            else:
                dp[i][w] = dp[i-1][w]

    # Визначення набору страв, що максимізують калорійність
    w = budget
    n = len(items)
    chosen_items = []
    while w >= 0 and n > 0:
        if dp[n][w] != dp[n-1][w]:
            item_name, item_details = item_list[n-1]
            chosen_items.append(item_name)
            w -= item_details['cost']
        n -= 1

    return chosen_items, dp[-1][-1]

# Тестування алгоритмів
budget = 100
greedy_items, greedy_calories = greedy_algorithm(items, budget)
dp_items, dp_calories = dynamic_programming(items, budget)

greedy_items, greedy_calories, dp_items, dp_calories

import random

def simulate_ball_extraction(a, b, num_simulations):
    first_white_count = 0
    last_white_count = 0

    for _ in range(num_simulations):
        # Создаем список шаров: 'W' для белого и 'B' для черного
        urn = ['W'] * a + ['B'] * b
        random.shuffle(urn)  # Перемешиваем шары

        # Проверяем, является ли первый шар белым
        if urn[0] == 'W':
            first_white_count += 1

        # Проверяем, является ли последний шар белым
        if urn[-1] == 'W':
            last_white_count += 1

    # Вычисляем вероятности
    prob_first_white = first_white_count / num_simulations
    prob_last_white = last_white_count / num_simulations

    return prob_first_white, prob_last_white

# Параметры симуляции
a = 5  # количество белых шаров
b = 5  # количество черных шаров
num_simulations = 100000  # количество симуляций

prob_first_white, prob_last_white = simulate_ball_extraction(a, b, num_simulations)

print(f"Вероятность того, что первый шар белый: {prob_first_white:.4f}")
print(f"Вероятность того, что последний шар белый: {prob_last_white:.4f}")

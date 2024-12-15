import numpy as np
from math import comb

def probability_at_least_one_winning(n, k):
    if n <= 2 * k:
        raise ValueError("n должно быть больше 2k.")

    # Общее количество способов выбрать k билетов из n
    total_ways = comb(n, k)

    # Количество способов выбрать k билетов без выигрышных
    non_winning_ways = comb(n - k, k)

    # Вероятность того, что среди k купленных билетов нет выигрышных
    probability_no_winning = non_winning_ways / total_ways

    # Вероятность того, что хотя бы один билет выигрышный
    probability_at_least_one_winning = 1 - probability_no_winning

    return probability_at_least_one_winning

# Пример использования
n = 100  # Общее количество билетов
k = 10   # Количество выигрышных билетов

probability = probability_at_least_one_winning(n, k)
print(f"Вероятность того, что среди {k} купленных билетов по крайней мере один будет выигрышным: {probability:.4f}")

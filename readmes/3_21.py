import math

def combinations(n, r):
    """Вычисление сочетаний C(n, r)"""
    if r > n or r < 0:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def probability_kth_ball_white(a, b, k):
    """Вычисление вероятности того, что k-й шар белый"""
    if k > a + b or k < 1:
        return 0  # Невозможно, если k больше общего количества шаров

    # Количество способов выбрать 1 белый шар и (k-1) черных
    favorable_outcomes = combinations(a, 1) * combinations(b, k - 1)

    # Общее количество способов выбрать k шаров из (a + b)
    total_outcomes = combinations(a + b, k)

    # Вероятность
    probability = favorable_outcomes / total_outcomes
    return probability

# Параметры
a = 5  # количество белых шаров
b = 5  # количество черных шаров
k = 3  # номер шара, который мы хотим проверить

prob = probability_kth_ball_white(a, b, k)
print(f"Вероятность того, что {k}-й шар белый: {prob:.4f}")

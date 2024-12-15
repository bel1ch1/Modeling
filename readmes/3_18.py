import numpy as np

def factorial(n):
    """Вычисление факториала n! с использованием NumPy."""
    return np.math.factorial(n)

def multinomial_coefficient(counts):
    """Вычисление мультикомбинаторного коэффициента."""
    total = np.sum(counts)
    numerator = factorial(total)
    denominator = np.prod([factorial(count) for count in counts])
    return numerator // denominator

def calculate_probability():
    # Заданные параметры
    total_balls = 30
    total_boxes = 8

    # Распределение: [0, 0, 3, 3, 6, 6, 12, 0] (3 пустых, 2 с 3, 2 с 6, 1 с 12)
    distribution = np.array([0, 0, 3, 3, 6, 6, 12, 0])

    # Количество благоприятных исходов
    favorable_outcomes = multinomial_coefficient(distribution)

    # Общее количество исходов (каждый шар может попасть в любой из 8 ящиков)
    total_outcomes = total_boxes ** total_balls

    # Вероятность
    probability = favorable_outcomes / total_outcomes
    return probability

# Вычисляем вероятность
probability = calculate_probability()
print(f"Вероятность размещения: {probability:.10f}")

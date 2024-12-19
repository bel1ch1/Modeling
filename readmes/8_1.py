import math

# Среднее число вызовов за 2 минуты
lambda_ = 6

# Функция для вычисления вероятности по формуле Пуассона
def poisson_probability(k, lambda_):
    return (lambda_**k * math.exp(-lambda_)) / math.factorial(k)

# а) Вероятность того, что за 2 минуты поступит 2 вызова
k_a = 2
prob_a = poisson_probability(k_a, lambda_)
print(f"Вероятность того, что за 2 минуты поступит 2 вызова: {prob_a:.4f}")

# б) Вероятность того, что за 2 минуты поступит меньше 2 вызовов (k = 0 и k = 1)
prob_b = poisson_probability(0, lambda_) + poisson_probability(1, lambda_)
print(f"Вероятность того, что за 2 минуты поступит меньше 2 вызовов: {prob_b:.4f}")

# в) Вероятность того, что за 2 минуты поступит не менее 2 вызовов
prob_c = 1 - prob_b  # Это 1 минус вероятность меньше 2 вызовов
print(f"Вероятность того, что за 2 минуты поступит не менее 2 вызовов: {prob_c:.4f}")

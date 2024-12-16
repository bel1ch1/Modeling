from scipy.optimize import linprog
import time

start = time.time()

# Измененные коэффициенты функции цели
c = [-40, -2]  # Функция цели

# Измененные неравенства
A_ub = [[100, 10]]  # Новые коэффициенты для неравенства
b_ub = [50000]      # Новое значение для неравенства

# Измененные равенства
A_eq = [[4, -2]]    # Новые коэффициенты для равенства
b_eq = [0]          # Значение для равенства

# Решение задачи линейного программирования
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)

print(result)

stop = time.time()
print("Время :")
print(stop - start)

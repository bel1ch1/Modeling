import numpy as np
import matplotlib.pyplot as plt

# Определяем диапазон значений x1 и x2
x1 = np.linspace(0, 10, 400)

# Ограничение 1: 2x1 + x2 + x3 = 16 => x3 = 16 - 2x1 - x2
# Мы будем выражать x2 через x1 и x3
x2_1 = 16 - 2 * x1  # когда x3 = 0

# Ограничение 2: x1 - x2 <= 2 => x2 >= x1 - 2
x2_2 = x1 - 2

# Настройка графика
plt.figure(figsize=(10, 8))

# Параметры для построения графиков
plt.plot(x1, x2_1, label=r'\$2x_1 + x_2 + x_3 = 16$ (граничная)', color='blue')
plt.plot(x1, x2_2, label=r'$x_1 - x_2 = 2$ (граничная)', color='orange')

# Область допустимых решений
plt.fill_between(x1, np.maximum(0, x2_1), 10, where=(x2_1 >= 0) & (x2_2 <= x2_1), color='gray', alpha=0.5)

# Настройки графика
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.title('Графическое решение задачи линейного программирования')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.grid()

# Показать график
plt.show()

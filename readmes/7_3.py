import numpy as np
import matplotlib.pyplot as plt

# Определяем диапазон значений x1 и x2
x1 = np.linspace(0, 10, 400)
x2_1 = 3 * x1 - 6  # 3x1 - x2 > 6 => x2 < 3x1 - 6
x2_2 = 4 - 2 * x1  # 2x1 + x2 <= 4 => x2 <= 4 - 2x1
x2_3 = (x1 - 2) / 2  # x1 - 2x2 > 2 => x2 < (x1 - 2)/2

# Настройка графика
plt.figure(figsize=(10, 8))

# Параметры для построения графиков
plt.plot(x1, x2_1, label=r'\$3x_1 - x_2 = 6$ (граничная)', color='blue')
plt.plot(x1, x2_2, label=r'\$2x_1 + x_2 = 4$ (граничная)', color='orange')
plt.plot(x1, x2_3, label=r'$x_1 - 2x_2 = 2$ (граничная)', color='green')

# Область допустимых решений
plt.fill_between(x1, np.maximum(0, np.maximum(x2_1, x2_3)), 10, where=(x2_1 > 0) & (x2_3 > 0) & (x2_2 >= 0), color='gray', alpha=0.5)

# Настройки графика
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.title('Графическое решение задачи линейного программирования')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.grid()

# Показать график
plt.show()

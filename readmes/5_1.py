#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Измененные параметры электрической цепи
R1 = 15  # Сопротивление 1, Ом
R2 = 25  # Сопротивление 2, Ом
L = 0.03  # Индуктивность, Генри
C = 0.0001  # Ёмкость, Фарад
E = 120  # ЭДС, Вольт
tm = 0.05  # Время моделирования, секунды

def f(y, t):
    # Дифференциальное уравнение переходного процесса
    y1, y2 = y
    return [y2, -((L + R1 * R2 * C) / (R2 * L * C)) * y2 - ((R1 + R2) / (R2 * L * C)) * y1 + E / (L * C)]

# Временной массив
t = np.linspace(0, tm, 1000)
y0 = [E, 0]  # Начальные условия

# Решение дифференциального уравнения
z = odeint(f, y0, t)

# Вектор значений решения
y1 = z[:, 0]  # Напряжение на конденсаторе
y2 = 100 * (C * z[:, 1] + y1 / R2)  # Ток i1
y3 = 100 * C * z[:, 1]  # Ток i3
y4 = 100 * y1 / R2  # Ток i2

# Построение графиков
plt.title('Напряжение на конденсаторе и токи при замыкании цепи', size=12)
plt.plot(t * 1000, y1, linewidth=2, label='Uc(t)')
plt.plot(t * 1000, y2, linewidth=2, label='i1(t)*100')
plt.plot(t * 1000, y3, linewidth=2, label='i3(t)*100')
plt.plot(t * 1000, y4, linewidth=2, label='i2(t)*100')
plt.ylabel("Uc(t), i1(t), i2(t), i3(t)")
plt.xlabel("t (мс)")
plt.legend(loc='best')
plt.grid(True)
plt.show()

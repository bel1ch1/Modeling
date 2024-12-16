import numpy as np
import matplotlib.pyplot as plt

# Данные
R1 = R2 = R3 = 200  # Ом
L = 10              # Гн
I0 = 0.1            # Ампер (амплитуда тока)
frequency = 1000    # Гц (10^3)
phase_angle = np.radians(-30)  # Угол в радианах

# Временные параметры
time = np.linspace(0, 0.01, 1000)  # Время от 0 до 0.01 секунд

# Синусоидальный ток j(t)
j_t = I0 * np.sin(2 * np.pi * frequency * time + phase_angle)

# Используем закон Ома и формулу для тока в RL-цепи
# i_R1(t) = j(t) * R / (R + jωL)
omega = 2 * np.pi * frequency  # Угловая частота
Z = R1 + 1j * omega * L  # Импеданс
i_R1 = j_t / Z.real  # Ток через R1

# График
plt.figure(figsize=(10, 5))
plt.plot(time, i_R1, label='Ток через R1 (i_R1(t))')
plt.title('Ток через R1 во времени')
plt.xlabel('Время (с)')
plt.ylabel('Ток (A)')
plt.grid()
plt.legend()
plt.show()

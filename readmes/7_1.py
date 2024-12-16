import numpy as np
import matplotlib.pyplot as plt

# Данные
R1 = 200  # Ом
R2 = 100  # Ом
R3 = 200  # Ом
I = 10    # Ампер

# Вычисляем напряжение на каждом сопротивлении
U1 = I * R1
U2 = I * R2
U3 = I * R3

# Суммарное напряжение
U_total = U1 + U2 + U3

print(f"Напряжение на R1: {U1} В")
print(f"Напряжение на R2: {U2} В")
print(f"Напряжение на R3: {U3} В")
print(f"Общее напряжение в цепи: {U_total} В")

# Моделируем изменение напряжения на R3 во времени
time = np.linspace(0, 0.1, 1000)  # Время от 0 до 0.1 секунд
uR3 = U3 * np.sin(2 * np.pi * 10 * time)  # Моделируем синусоидальное напряжение

# График
plt.plot(time, uR3)
plt.title('Напряжение на R3 во времени')
plt.xlabel('Время (с)')
plt.ylabel('Напряжение (В)')
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def simulate_buses(num_simulations=1000):
    # Настройки
    bus_24_capacity = 30  # Вместимость 24-го автобуса
    bus_25_capacity = 30  # Вместимость 25-го автобуса
    avg_people_waiting = 20  # Среднее количество ожидающих людей

    # Счетчики переполненных автобусов
    full_bus_24_count = 0
    full_bus_25_count = 0

    for _ in range(num_simulations):
        # Случайное количество людей, ожидающих 24-й и 25-й автобусы
        people_waiting_24 = np.random.poisson(lam=avg_people_waiting)
        people_waiting_25 = np.random.poisson(lam=avg_people_waiting)

        # Проверка, переполнен ли 24-й автобус
        if people_waiting_24 > bus_24_capacity:
            full_bus_24_count += 1

        # Проверка, переполнен ли 25-й автобус
        if people_waiting_25 > bus_25_capacity:
            full_bus_25_count += 1

    return full_bus_24_count, full_bus_25_count

# Запуск симуляции
full_bus_24, full_bus_25 = simulate_buses()

# Вывод результатов
print(f"Количество переполненных 24-х автобусов: {full_bus_24}")
print(f"Количество переполненных 25-х автобусов: {full_bus_25}")

# Визуализация результатов
labels = ['24-й автобус', '25-й автобус']
counts = [full_bus_24, full_bus_25]

plt.bar(labels, counts, color=['blue', 'orange'])
plt.ylabel('Количество переполненных автобусов')
plt.title('Переполненные автобусы')
plt.show()

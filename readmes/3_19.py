import random

def simulate_team_grouping(num_simulations, n):
    same_group_count = 0
    different_group_count = 0

    for _ in range(num_simulations):
        # Создаем список команд (от 1 до 2n)
        teams = list(range(1, 2 * n + 1))
        # Перемешиваем команды
        random.shuffle(teams)

        # Разбиваем на две подгруппы
        group1 = teams[:n]
        group2 = teams[n:]

        # Проверяем, в одной ли подгруппе две сильнейшие команды (например, 1 и 2)
        if 1 in group1 and 2 in group1:
            same_group_count += 1
        elif 1 in group2 and 2 in group2:
            same_group_count += 1
        else:
            different_group_count += 1

    return same_group_count, different_group_count

# Параметры симуляции
n = 5  # количество команд в каждой подгруппе (всего 2n = 10 команд)
num_simulations = 100000  # количество симуляций

same_group_count, different_group_count = simulate_team_grouping(num_simulations, n)

# Вычисляем вероятности
total_count = same_group_count + different_group_count
prob_same_group = same_group_count / total_count
prob_different_group = different_group_count / total_count

print(f"Количество случаев, когда команды в одной подгруппе: {same_group_count}")
print(f"Количество случаев, когда команды в разных подгруппах: {different_group_count}")
print(f"Вероятность того, что команды в одной подгруппе: {prob_same_group:.4f}")
print(f"Вероятность того, что команды в разных подгруппах: {prob_different_group:.4f}")

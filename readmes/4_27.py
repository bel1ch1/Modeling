def calculate_probabilities():
    # Событие A: хотя бы одна единица при 4 бросках
    p_no_one_in_four = (5/6)**4
    p_at_least_one_one = 1 - p_no_one_in_four

    # Событие B: хотя бы одна пара единиц при 24 бросках по 2 кости
    p_no_double_one = (35/36)
    p_no_double_one_in_24 = p_no_double_one**24
    p_at_least_one_double_one = 1 - p_no_double_one_in_24

    return p_at_least_one_one, p_at_least_one_double_one

# Вычисление вероятностей
prob_A, prob_B = calculate_probabilities()

# Вывод результатов
print(f"Вероятность получить хотя бы одну единицу при 4 бросках: {prob_A:.4f}")
print(f"Вероятность получить хотя бы одну пару единиц при 24 бросках: {prob_B:.4f}")

# Сравнение вероятностей
if prob_A > prob_B:
    print("Событие A более вероятно.")
elif prob_A < prob_B:
    print("Событие B более вероятно.")
else:
    print("Оба события имеют одинаковую вероятность.")

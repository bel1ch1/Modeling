# Определяем граф в виде словаря смежности
graph = {
    'I': ['II', 'III', 'V'],
    'II': ['I', 'III', 'IV'],
    'III': ['I', 'II', 'V'],
    'IV': ['II', 'V', 'VI'],
    'V': ['I', 'III', 'IV', 'VI'],
    'VI': []
}

# Функция для поиска всех простых путей от начальной до конечной точки
def all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)

    return paths

# Функция для расчета вероятности работы системы
def calculate_reliability(paths, p):
    reliability = 0
    for path in paths:
        # Вероятность успешной работы для каждого пути (умножаем вероятности всех рёбер на пути)
        path_reliability = p ** (len(path) - 1)
        reliability += path_reliability
    return reliability

# Основной блок программы
if __name__ == "__main__":
    start_node = 'I'
    end_node = 'VI'

    # Получаем все возможные пути от I до VI
    paths = all_paths(graph, start_node, end_node)
    print("Пути от I до VI:", paths)

    # Вероятности для различных p
    p_values = [0.9, 0.95]

    for p in p_values:
        system_reliability = calculate_reliability(paths, p)
        print(f"Вероятность работы системы при p={p}: {system_reliability:.4f}")

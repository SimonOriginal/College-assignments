#   Simon Bezruhenko
#   https://github.com/SimonW0rk
#   Решение задачи в Python!
#   Значення ймовірностей p^i, з якими дискретне джерело інформації генерує
#   символи алфавіту, для різних варіантів наведені у списку: "probabilities"
#   Побудувати нерівномірні ефективні коди за методиками Шеннона-Фано
#   для кодування символів джерела.

# Импортировать библиотеки networkx и matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Список вероятностей и соответствующих символов
probabilities = [(0.11, 'p1'), (0.16, 'p2'), (0.03, 'p3'), (0.26, 'p4'),
                 (0.04, 'p5'), (0.05, 'p6'), (0.03, 'p7'), (0.02, 'p8'), (0.30, 'p9')]

# Функция для вычисления кодов Шеннона-Фано


def shannon_fano(probabilities, prefix, codes):
    n = len(probabilities)
    # Добавляем код в словарь
    if n == 1:
        codes[probabilities[0][1]] = prefix
        return

    mid = n//2
    for i in range(mid):
        codes[probabilities[i][1]] = prefix + '0'
    shannon_fano(probabilities[:mid], prefix + '0', codes)

    for i in range(mid, n):
        codes[probabilities[i][1]] = prefix + '1'
    shannon_fano(probabilities[mid:], prefix + '1', codes)

# Функция для получения кодов с помощью функции shannon_fano


def induce_codes(probabilities):
    codes = dict()
    shannon_fano(sorted(probabilities, reverse=True), '', codes)
    return codes


# Получить коды для каждого символа
codes = induce_codes(probabilities)
# Распечатать коды для каждого символа
for character, code in codes.items():
    print(f"{character}: {code}({len(code)})")
# Распечатать отсортированный список вероятностей
print(f"Отсортированный список: {sorted(probabilities)}")

# Функция построения дерева для визуализации


def build_tree(probabilities, parent, graph):
    # Добавляем узел в граф
    if len(probabilities) == 1:
        graph.add_node(probabilities[0][1], label=probabilities[0][1])
        graph.add_edge(parent, probabilities[0][1])
        return

    mid = len(probabilities) // 2
    left = probabilities[:mid]
    right = probabilities[mid:]

    node_left = f"{parent}0"
    node_right = f"{parent}1"
    # Добавляем узлы в граф
    graph.add_node(node_left, label=node_left)
    graph.add_node(node_right, label=node_right)
    graph.add_edge(parent, node_left)
    graph.add_edge(parent, node_right)

    build_tree(left, node_left, graph)
    build_tree(right, node_right, graph)

# Функция для визуализации дерева


def visualize_tree(codes):
    # Сортировка кодов по их длине
    probabilities = sorted([(len(code), char)
                           for char, code in codes.items()], reverse=True)
    graph = nx.DiGraph()
    build_tree(probabilities, '', graph)
    # Рисуем граф дерева с помощью библиотеки NetworkX
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=True)
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw_networkx_labels(graph, pos, labels)

    plt.show()
# Рассчитать среднюю длину кодового слова для кодов


def calculate_average_codeword_length(codes, probabilities):
    total_length = 0
    for character, code in codes.items():
        for prob in probabilities:
            if prob[1] == character:
                total_length += len(code) * prob[0]
                break
    return total_length


average_codeword_length = calculate_average_codeword_length(
    codes, probabilities)
print("Средняя длина кодового слова:", average_codeword_length)

# Повторно сгенерировать коды и визуализировать дерево
codes = induce_codes(probabilities)
visualize_tree(codes)

input("Нажмите Enter, чтобы выйти...")

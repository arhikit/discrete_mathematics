# функция возвращает количество компонент связности
# входные данные: список смежности графа
def count_of_connected_components(graph):
    def visit(v):
        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                visit(w)

    visited = [0 for _ in range(len(graph))]
    cc = 0

    for i in range(len(graph)):
        if not visited[i]:
            visit(i)
            cc += 1

    return cc


# функция проверяет, есть ли в графе вершина с нечетной степенью
# входные данные: список смежности графа
def is_odd_vertex(graph):
    for w in graph:
        if len(w) % 2 == 1:
            return True
    return False


# функция проверяет, является ли граф Эйлеровым
# входные данные: список смежности графа
def is_eulerian(graph):

    # количество компонент связности должно быть равно 1
    if count_of_connected_components(graph) > 1:
        return False

    # степени всех вершин должны быть четными
    elif is_odd_vertex(graph):
        return False

    return True


# функция выводит Эйлеров цикл
# входные данные: список смежности графа
def eulerial_cycle(graph):
    def remove_edge(i, j):
        graph[i].remove(j)
        graph[j].remove(i)

    def visit(v):
        for w in graph[v]:
            remove_edge(w, v)
            visit(w)
        cycle.append(v + 1)

    cycle = []

    # запускаем обход графа с вершины 0
    visit(0)

    # выводим цикл в обратном порядке
    return cycle[:-1]

# Функция находит Эйлеров цикл
# Выходные данные: NONE, если в графе нет эйлерова цикла,
# или список вершин в порядке обхода эйлерова цикла, если он есть.
def get_eulerial_cycle(v, edges):

    # строим список смежности графа
    graph = [[] for _ in range(v)]
    for x, y in edges:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    # проверяем, является ли граф Эйлеровым
    if is_eulerian(graph):
        # получаем Эйлеров цикл
        return ' '.join(map(str, eulerial_cycle(graph)))
    else:
        return 'NONE'


def main():
    # считываем чиcло вершин и число ребер графа
    v, e = map(int, input().split())

    # считываем ребра графа
    edges = []
    for _ in range(e):
        x, y = map(int, input().split())
        edges.append((x, y))

    print(get_eulerial_cycle(v, edges))


def test():
    assert get_eulerial_cycle(4, [(1, 2), (3, 2)]) == 'NONE'
    assert get_eulerial_cycle(3, [(1, 2), (2, 3), (3, 1)]) == '1 3 2'


if __name__ == "__main__":
    main()
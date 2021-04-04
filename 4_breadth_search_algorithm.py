# функция возвращает расстояния от вершины 0 до всех вершин графа
# входные данные: число вершин, список ребер
def get_distance_from_0(v, edges):

    # строим список смежности графа
    graph = [[] for _ in range(v)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    # инициализируем вершину, от которой будем искать расстояния до всех вершин графа
    init_v = 0

    # отмечаем все вершины как непосещенные
    visited = [0 for _ in range(len(graph))]
    # инициализируем расстояния от вершины init_v до соответствующей вершины
    distance = [0 for _ in range(len(graph))]
    # инициализируем очередь вершиной init_v, текущая позиция в очереди = 0
    queue, curr_num = [init_v], 0

    # пока есть необработанные элементы в очереди
    while curr_num < len(queue):
        # берем из очереди левый элемент. отмечаем его как посещенный
        v = queue[curr_num]
        visited[v] = 1

        # идем по списку смежности выбранного элемента
        for w in graph[v]:
            # если вершина еще не посещена и ее нет в очереди,
            # то добавляем ее в очередь
            # и записываем расстояние до нее = расстояние до текущей вершины + 1
            if not visited[w] and not w in queue:
                queue.append(w)
                distance[w] = distance[v] + 1

        # увеличиваем счетчик очереди
        curr_num += 1

    return ' '.join(map(str, distance))

def main():
    # считываем чиcло вершин и число ребер графа
    v, e = map(int, input().split())

    # считываем ребра графа
    edges = []
    for _ in range(e):
        x, y = map(int, input().split())
        edges.append((x, y))

    print(get_distance_from_0(v, edges))


def test():
    assert get_distance_from_0(6, [(0, 1), (1, 2), (2, 0), (3, 2), (4, 3), (4, 2), (5, 4)]) == "0 1 1 2 2 3"


if __name__ == "__main__":
    main()
# функция возвращает количество компонент связности графа
# входные данные: число вершин, список ребер
def get_count_of_connected_components(v, edges):

    def visit(v):
        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                visit(w)

    # строим список смежности графа
    graph = [[] for _ in range(v)]
    for x, y in edges:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    # отмечаем все вершины как непосещенные
    visited = [0 for _ in range(len(graph))]
    # инициализируем количество компонент связности
    cc = 0

    # проходим по всем вершинам, начиная с 0 вершины и рекурсивно обходим во всем смежным вершинам.
    # если остаются непосещенные вершины, то запускаем процесс заново, увеличивая количество компонент связности
    for i in range(len(graph)):

        if not visited[i]:
            visit(i)
            cc += 1

    return cc


def main():
    # считываем чиcло вершин и число ребер графа
    v, e = map(int, input().split())

    # считываем ребра графа
    edges = []
    for _ in range(e):
        x, y = map(int, input().split())
        edges.append((x, y))

    print(get_count_of_connected_components(v, edges))


def test():
    assert get_count_of_connected_components(4, [(1, 2), (3, 2)]) == 2
    assert get_count_of_connected_components(4, [(1, 2), (3, 2), (4, 3)]) == 1


if __name__ == "__main__":
    main()
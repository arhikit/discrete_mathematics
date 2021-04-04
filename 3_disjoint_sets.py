def Find(i, parent):
    while i != parent[i - 1]:
        i = parent[i - 1]
    return i

def Union(i, j, parent, rank):
    i_id = Find(i, parent)
    j_id = Find(j, parent)
    if i_id == j_id:
        return
    if rank[i_id - 1] > rank[j_id - 1]:
        parent[j_id - 1] = i_id
    else:
        parent[i_id - 1] = j_id
        if rank[i_id - 1] == rank[j_id - 1]:
            rank[j_id - 1] += 1

# функция возвращает количество компонент связности графа
# входные данные: число вершин, список ребер
def get_count_of_connected_components(v, edges):

    parent = [(i + 1) for i in range(v)]
    rank = [0 for i in range(v)]

    for i, j in edges:
        Union(i, j, parent, rank)

    ans = set()
    for i in set(parent):
        if i == parent[i-1]:
            ans.add(i)

    return len(ans)


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
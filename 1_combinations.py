def get_combinations(k, n):

    combinations = []

    # инициализируем первое сочетание
    a = [i for i in range(k)]
    combinations.append(" ".join(map(str, a)))

    # последовательно (по возрастанию) перебираем все сочетания
    def one(a, k, n):
        for i in range(k - 1, -1, -1):
            if a[i] < (n - 1) - (k - 1 - i):
                a[i] += 1
                for j in range(i + 1, k):
                    a[j] = a[j - 1] + 1
                combinations.append(" ".join(map(str, a)))
                one(a, k, n)
    one(a, k, n)

    return combinations


# используем стандартную библиотеку
def get_combinations2(k, n):
    from itertools import combinations

    c = []
    for item in combinations(''.join([str(i) for i in range(n)]), k):
        c.append(' '.join(item))

    return c


def main():
    # считываем два числа k и n
    k, n = map(int, input().split())

    # выводим построчно k-сочетания из n элементов
    print("\n".join(get_combinations(k, n)))


def test():
    assert get_combinations(2, 3) == ["0 1", "0 2", "1 2"]
    assert get_combinations(1, 1) == ["0"]


if __name__ == '__main__':
    main()
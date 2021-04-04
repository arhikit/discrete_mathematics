def get_permutations(n, k):

    permutations = []

    # генерация всех перестановок с использованием рекурсии
    def genPermut(permut):
        if len(permut) == k:
            permutations.append(" ".join(map(str, permut)))
        else:
            for i in range(n):
                if i not in permut:
                    new_permut = permut + (i,)
                    genPermut(new_permut)

    genPermut(())
    return permutations


def main():
    # считываем два числа n и k
    n, k = map(int, input().split())

    # выводим построчно k-перестановки из n элементов
    print("\n".join(get_permutations(n, k)))


def test():
    assert get_permutations(4, 2) == ["0 1", "0 2", "0 3", "1 0", "1 2", "1 3", "2 0", "2 1", "2 3", "3 0", "3 1", "3 2"]


if __name__ == '__main__':
    main()
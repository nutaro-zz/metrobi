def find_duplicated(array: list) -> list:
    duplicated = list()
    for k, v in enumerate(array):
        if v in duplicated:
            continue
        for i, x in enumerate(array):
            if k == i or v != x:
                continue
            duplicated.append(x)
            break
    return duplicated


if __name__ == '__main__':
    print(find_duplicated([1, 2, 3, 2, 1, 5, 6, 5, 5, 5]))

def counting_rhyme(n: int, k: int) -> int:
    arr = [i for i in range(1, n + 1)]
    while len(arr) > 1:
        for _ in range(k - 1):
            skip = arr.pop(0)
            arr.append(skip)
        arr.pop(0)
    return arr[0]


if __name__ == '__main__':
    print(counting_rhyme(7, 5))

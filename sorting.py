from typing import List
from random import randint


def small_sort(arr: List[int]) -> List[int]:
    """
    Сортирует массив целых чисел ограниченного диапазона значений
    :param arr: исходный массив целых чисел
    :return: отсортированный массив целых чисел
    """
    start = min(arr)
    stop = max(arr)
    d = {i: 0 for i in range(start, stop + 1)}
    for i in arr:
        d[i] = d.get(i) + 1
    result = []
    for i in d:
        result += [i] * d[i]
    return result


if __name__ == '__main__':
    nums = small_sort([randint(13, 25) for _ in range(10 ** 4)])

    print(nums)

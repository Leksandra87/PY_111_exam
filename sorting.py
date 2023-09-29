from typing import List
from random import randint


def small_sort(arr: List[int]) -> List[int]:
    """
    Сортирует массив целых чисел ограниченного диапазона значений
    :param arr: исходный массив целых чисел
    :return: отсортированный массив целых чисел
    """
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    d_sort = sorted(d.items())
    result = []
    for i in d_sort:
        result += [i[0]] * i[1]
    return result


if __name__ == '__main__':
    nums = [randint(13, 25) for _ in range(10 ** 6)]
    print(small_sort(nums))


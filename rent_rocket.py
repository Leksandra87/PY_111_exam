from typing import Tuple, List


def rent_time(schedule: List[Tuple[int, int]]) -> bool:
    num = len(schedule)  # количество заявок на полет
    flag = True
    for i in range(num - 1):
        if schedule[i][1] > schedule[i + 1][0]:
            flag = False
    return flag


if __name__ == '__main__':
    arr = [(10, 12), (12, 13), (15, 19), (22, 23),(18, 22)]
    print(rent_time(arr))


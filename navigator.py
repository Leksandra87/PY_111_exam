from typing import Tuple, List


def navigate(field: List[List[int]], start: Tuple[int, int], stop: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Найти самый дешёвый путь из точки старт в точку стоп на пронумерованной плоскости
    :param field: поле с заданными стоимостями посещения каждой ячейки
    :param start: координаты начала пути
    :param stop: координаты окончания пути
    :return:
    """
    rows = len(field)  # количество строк (y)
    columns = len(field[0])  # количество столбцов (x)
    visited = [[False] * columns for _ in range(rows)]
    rout_cost = [[float('inf')] * columns for _ in range(rows)]
    rout_cost[start[0]][start[1]] = 0
    way = [[None] * columns for _ in range(rows)]
    d = {0: start}

    while d:
        c_cost, c_pos = min(d.items())
        d.pop(c_cost)
        if c_pos == stop:
            break
        if visited[c_pos[0]][c_pos[1]]:
            continue
        visited[c_pos[0]][c_pos[1]] = True

        for next_p in check_neighbor(c_pos, rows, columns):
            cost = field[next_p[0]][next_p[1]]

            if c_cost + cost < rout_cost[next_p[0]][next_p[1]]:
                rout_cost[next_p[0]][next_p[1]] = c_cost + cost
                way[next_p[0]][next_p[1]] = c_pos
                d[rout_cost[next_p[0]][next_p[1]]] = next_p
    rout = []
    last_pos = stop
    while last_pos is not None:
        rout.append(last_pos)
        last_pos = way[last_pos[0]][last_pos[1]]

    return rout[::-1]


def check_neighbor(pos: Tuple[int, int], c: int, r: int) -> List[Tuple[int, int]]:
    row, col = pos
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < r - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < c - 1:
        neighbors.append((row, col + 1))

    return neighbors


if __name__ == '__main__':
    arr = [
        [2, 1, 3, 8],
        [4, 1, 2, 5],
        [6, 1, 3, 7],
        [6, 1, 3, 7]
    ]
    st = (3, 3)
    e = (0, 0)
    print(navigate(arr, st, e))

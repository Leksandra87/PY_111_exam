from typing import List


def consensus(dna_reads: List[str]) -> str:
    """
    Построение консенсус-строки из списка строк одинаковой длины
    :param dna_reads: список исходных строк
    :return: консенсус-строка
    """
    m = len(dna_reads[0])  # длина строки
    n = len(dna_reads)  # количество строк
    result = ''
    for i in range(m):
        d = {}
        for j in range(n):
            d[dna_reads[j][i]] = d.get(dna_reads[j][i], 0) + 1
        result += max(d.items(), key=lambda x: x[1])[0]
    return result


if __name__ == '__main__':
    arr = ['ATTAATTA',
           'ACTAATCA',
           'AGCAACGA',
           'ACAAAACA']
    print(consensus(arr))

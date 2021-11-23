#
# for x in tableau:
#     if x > i and x % i == 0:
#         tableau.remove(x)

def primeNumber(limit: int) -> [int]:
    primeArr = [True] * (limit + 1)
    idx = 2

    while idx ** 2 <= limit:
        if primeArr[idx]:
            index_multiple = 2 * idx
            while index_multiple <= limit:
                primeArr[index_multiple] = False
                index_multiple += idx

        idx += 1

    primeList = []
    idx = 2
    while idx <= limit:
        if primeArr[idx]:
            primeList.append(idx)
        idx += 1

    return primeList


print(primeNumber(100))

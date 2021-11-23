def searchInOrderedList(source: [int], target: int) -> int:
    index_inf = 0
    index_sup = len(source) - 1

    while index_inf <= index_sup:
        index_test = (index_sup + index_inf) // 2

        if source[index_test] == target:
            return index_test
        elif source[index_test] > target:
            index_sup = index_test - 1
        else:
            index_inf = index_test + 1

    return -1


print(searchInOrderedList([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 20))

def retrieve_list_pattern(list_int: [int], pattern: [int]) -> int:
    len_source = len(list_int)
    len_target = len(pattern)
    index_source = 0
    while index_source <= (len_source - len_target):
        index_target = 0
        idx_test = index_source
        while index_target < len_target and pattern[index_target] == list_int[idx_test]:
            index_target += 1
            idx_test += 1

        if index_target == len_target:
            return index_source

        index_source += 1

    return -1


print(retrieve_list_pattern([391, 131, 719, 170, 658], [719, 170]))

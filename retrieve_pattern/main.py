def retrieve_list_pattern(list_int: [int], pattern: [int]) -> int:
    main_list_idx = 0
    pattern_idx = 0
    finded_idx = 0
    while main_list_idx < len(list_int):
        if list_int[main_list_idx] == pattern[pattern_idx]:
            finded_idx = main_list_idx
            while pattern_idx < len(pattern):
                if list_int[main_list_idx] == pattern[pattern_idx]:
                    pattern_idx += 1
                    main_list_idx += 1
                else:
                    pattern_idx = 0
                    finded_idx = -1
                    break

        main_list_idx += 1
    return finded_idx


print(retrieve_list_pattern([391, 131, 719, 170, 658], [719, 170]))

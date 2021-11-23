def reverse_list(list_int: [int]) -> [int]:
    idx_left = 0
    idx_right = len(list_int) - 1
    while idx_right > idx_left:
        tmp = list_int[idx_left]
        list_int[idx_left] = list_int[idx_right]
        list_int[idx_right] = tmp
        idx_left += 1
        idx_right -= 1

    return list_int


def reverse_list_simple(list_int: [int]) -> [int]:
    idx = 0
    reversed_list = []
    while idx < len(list_int):
        reversed_list.insert(0, list_int[idx])
        idx += 1
    return reversed_list


print('reverse list : ', reverse_list([-20, 2, -5, 10, 12]))
print('reverse list simple : ', reverse_list_simple([-20, 2, -5, 10, 12]))

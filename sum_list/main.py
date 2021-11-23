import functools


def sum_list(list_integer: [int]) -> int:
    idx, sigma = 0, 0
    while idx < len(list_integer):
        sigma += list_integer[idx]
        idx += 1
    return sigma


def sum_list_reduce(list_int: [int]) -> int:
    return functools.reduce(lambda a, b: a + b, list_int)


def sum_list_even_ood(list_integer: [int]) -> (int, int):
    idx, sigma_even, sigma_odd = 0, 0, 0
    while idx < len(list_integer):
        if list_integer[idx] % 2 == 0:
            sigma_even += list_integer[idx]
        else:
            sigma_odd += list_integer[idx]
        idx += 1
    return sigma_even, sigma_odd


def min_max(list_int: [int]) -> (int, int):
    idx = 0
    _min = list_int[idx]
    _max = list_int[idx]
    while idx < len(list_int):
        if list_int[idx] < _min:
            _min = list_int[idx]
        if list_int[idx] > _max:
            _max = list_int[idx]
        idx += 1

    return _min, _max


def max_delta_between_consecutive_element(list_int: [int]) -> int:
    idx = 0
    delta = list_int[0] - list_int[1]
    while idx < len(list_int) - 1:
        step = list_int[idx + 1] - list_int[idx]
        if step > delta:
            delta = step
        idx += 1

    return delta



print('sum_list =>', sum_list([1, 2, 3]))
print('sum_list_reduce =>', sum_list_reduce([1, 2, 3]))
print('sum_list_even_ood =>', sum_list_even_ood([1, 2, 3]))
print('min_max =>', min_max([-20, 2, -5, 10, 12]))
print('max_delta_between_consecutive_element =>', max_delta_between_consecutive_element([-20, 2, -5, 10, 12]))

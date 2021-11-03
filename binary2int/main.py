from typing import List

def binary2decimal(binary_arr: List[int]) -> int:
    dec_value = 0
    for bit in binary_arr:
        dec_value *= 2
        dec_value += bit

    return dec_value


print(binary2decimal([1, 1, 1, 1, 1, 1, 1, 1]))

def binary2decimal_correction(binary_arr: [int]) -> int:
    dec_value = 0
    for bit in binary_arr:
        dec_value <<= 1  # dec_value *= 2

        dec_value += bit

    return dec_value


print(binary2decimal_correction([1, 1, 1, 1, 1, 1, 1, 1]))

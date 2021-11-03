def dec2bin(decimal_value: int) -> [int]:
    binary_value = [decimal_value & 1]
    decimal_value >>= 1
    while decimal_value > 0:
        binary_value.insert(0, decimal_value & 1)
        decimal_value >>= 1

    return binary_value


print(dec2bin(12))

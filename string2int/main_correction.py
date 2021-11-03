def string2int_correc(num: str) -> int:
    dec_value = 0
    for char in num:
        dec_value *= 10
        dec_value += ord(char) - ord('0')

    return dec_value


print(string2int_correc('19821121'))

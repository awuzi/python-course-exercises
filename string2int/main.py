def string2int(num_string: str) -> int:
    ASCII_BASE = 48
    result = 0
    for current_idx, char in enumerate(num_string):
        reversed_idx = len(num_string) - 1
        num_char = ord(char) - ASCII_BASE
        result += num_char * pow(10, reversed_idx - current_idx)
    return result


print(string2int('19821121'))

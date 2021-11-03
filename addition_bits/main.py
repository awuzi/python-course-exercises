_xor = lambda a, b: a ^ b
# def _xor(a: int, b: int) -> int:
#     return a ^ b

_and = lambda a, b: a & b
# def _and(a: int, b: int) -> int:
#     return a & b

_or = lambda a, b: a | b
# def _or(a: int, b: int) -> int:
#     return a | b


def add_two_bits(a: int, b: int, carry: int):
    """
    :param a: bit
    :param b: bit
    :param carry: cost when 1 + 1
    :return: operation and carry
    """
    res: int = _xor(_xor(a, b), carry)
    carry: int = _or(_and(_xor(a, b), carry), _and(a, b))

    return res, carry


def add_two_binay_num(a: str, b: str) -> [int]:
    carry = 0
    result = []
    reversed_idx = len(a) - 1
    for (idx, elem) in enumerate(a):
        first_bit = int(a[reversed_idx - idx])
        second_bit = int(b[reversed_idx - idx])
        operation_result, cost = add_two_bits(first_bit, second_bit, carry)
        carry = cost
        result.insert(0, operation_result)

    return result


print(add_two_binay_num('1100', '1010'))

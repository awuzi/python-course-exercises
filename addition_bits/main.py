from typing import List


def _xor(a: int, b: int) -> int:
    return a ^ b


def _and(a: int, b: int) -> int:
    return a & b


def _or(a: int, b: int) -> int:
    return a | b


def add_two_bits(a: int, b: int, carry: int):
    res: int = _xor(_xor(a, b), carry)
    carry: int = _or(_and(_xor(a, b), carry), _and(a, b))

    return res, carry


def add_two_binay_num(a: str, b: str) -> List[int]:
    carry = 0
    result = []
    for (elem_a, elem_b) in zip(a, b):
        [operation_result, cost] = add_two_bits(int(elem_a), int(elem_b), carry)
        carry = cost
        result.insert(0, operation_result)

    if carry != 0:
        result.insert(0, carry)

    return result


print(add_two_binay_num('1001', '1011'))

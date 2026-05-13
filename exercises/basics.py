from typing import List

def collatz(n: int) -> List[int]:
    """
    Generate the Collatz sequence starting from n until reaching 1.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def distinct_numbers(numbers: List[int]) -> int:
    """
    Return the number of distinct/unique integers in the list.
    """
    return len(set(numbers))

"""
Project Euler Problem 1: Multiples of 3 or 5
URL: https://projecteuler.net/problem=1

Author: Francisco Ruvalcaba
Date: 2025-10-10
"""

def is_multiple_of_3_or_5(n: int) -> bool:
    """
    Checks if n is a multiple of 3 or 5.

    Args:
        n (int): The number to check

    Returns:
        bool: True if n is a multiple of 3 or 5, False otherwise
    """
    return n % 3 == 0 or n % 5 == 0

def solve(limit: int = 1000) -> int:
    """
    Calculates the sum of all multiples of 3 or 5 below 'limit'.

    Args:
        limit (int): The exclusive upper bound for checking

    Returns:
        int: The sum of all qualifying multiples
    """
    answer = 0
    for number in range(1, limit):
        if is_multiple_of_3_or_5(number):
            answer += number
    return answer

if __name__ == "__main__":
    solution = solve(1000)
    print(f"The solution for problem 1 is: {solution}")

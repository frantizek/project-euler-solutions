"""
Project Euler Problem 2: Even Fibonacci numbers
URL: https://projecteuler.net/problem=2

Author: Francisco Ruvalcaba
Date: 2025-10-10
"""

def fibonacci_generator():
    """
    Generator yielding an infinite sequence of Fibonacci numbers.

    Yields:
        int: The next Fibonacci number in the sequence
    """
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def is_even(n: int) -> bool:
    """
    Checks if an integer is even.

    Args:
        n (int): The integer to check

    Returns:
        bool: True if n is even, False otherwise
    """
    return n % 2 == 0

def solve(limit: int = 4_000_000) -> int:
    """
    Calculates the sum of even Fibonacci numbers below 'limit'.

    Args:
        limit (int): The exclusive upper bound for Fibonacci numbers

    Returns:
        int: The sum of all even Fibonacci numbers under the limit
    """
    fib_gen = fibonacci_generator()
    answer = 0
    fib_num = next(fib_gen)
    while fib_num < limit:
        if is_even(fib_num):
            answer += fib_num
        fib_num = next(fib_gen)
    return answer

if __name__ == "__main__":
    solution = solve(4000000)
    print(f"The solution for problem 2 is: {solution}")

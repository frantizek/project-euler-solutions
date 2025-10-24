"""
Project Euler Problem 3: Largest prime factor
URL: https://projecteuler.net/problem=3

Author: Francisco Ruvalcaba
Date: 2025-10-10
"""


def is_prime(n: int) -> bool:
    """
    Checks if n is a prime integer.

    Args:
        n (int): Value to check

    Returns:
        bool: True if n is prime, otherwise False
    """

    # what a prime number is
    # A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    #
    # So:
    #
    # Numbers ≤ 1 → not prime
    # 2 → prime (the only even prime)
    # Even numbers > 2 → not prime
    # Odd numbers > 2 → need to check for divisors

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd factors from 3 up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of integer n by checking factors
    and using the is_prime helper function.

    Args:
        n (int): Target number to factor

    Returns:
        int: Largest prime factor
    """
    largest_p_factor = 1

    # Iterate through all numbers up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i is a factor of n
        if n % i == 0:
            # We have a pair of factors: i and (n / i)

            # Check the smaller factor, i
            if is_prime(i):
                largest_p_factor = max(largest_p_factor, i)

            # Check the larger factor, (n / i)
            other_factor = n // i
            if is_prime(other_factor):
                largest_p_factor = max(largest_p_factor, other_factor)

    # This handles the case where n itself is a prime number
    if largest_p_factor == 1 and is_prime(n):
        return n

    return largest_p_factor

def solve(number: int = 600851475143) -> int:
    """
    Solves the Project Euler problem for the given number.

    Args:
        number (int): The target number for the problem

    Returns:
        int: The largest prime factor
    """
    return largest_prime_factor(number)

if __name__ == "__main__":
    solution = solve(600851475143)
    print(f"The solution for problem 3 is: {solution}")

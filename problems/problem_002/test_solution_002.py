"""
Unit tests for Project Euler Problem 2.
"""
import pytest
from solution_002 import solve, fibonacci_generator, is_even

def test_fibonacci_sequence():
    """
    Basic checks for the Fibonacci generator.
    """
    fib_gen = fibonacci_generator()
    sequence = [next(fib_gen) for _ in range(10)]
    assert sequence == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_is_even_function():
    """
    Ensure is_even works on positives, zero, and negatives.
    """
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)
    assert is_even(-4)
    assert not is_even(-5)

def test_small_limit():
    """
    For limit=10, even Fibonacci numbers are [2, 8].
    Sum should be 10.
    """
    assert solve(10) == 10

def test_project_euler_answer():
    """
    The official Project Euler answer with limit = 4_000_000.
    """
    expected_answer = 4613732
    assert solve(4000000) == expected_answer

"""
Unit tests for Project Euler Problem 3.
"""
import pytest
from solution_003 import solve, is_prime, largest_prime_factor

def test_is_prime_cases():
    """
    Quick validation for prime utility.
    """
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(100)
    assert is_prime(29)

def test_largest_prime_factor_sample():
    """
    For 13195, largest prime factor is known: 29.
    """
    assert largest_prime_factor(13195) == 29

def test_project_euler_answer():
    """
    Official Project Euler answer for 600851475143.
    """
    expected = 6857
    assert solve(600851475143) == expected

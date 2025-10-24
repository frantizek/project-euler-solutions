"""
Unit tests for Project Euler Problem 1.
"""
import pytest
from solution_001 import solve, is_multiple_of_3_or_5

def test_is_multiple_of_3_or_5():
    assert is_multiple_of_3_or_5(3)
    assert is_multiple_of_3_or_5(5)
    assert is_multiple_of_3_or_5(15)
    assert not is_multiple_of_3_or_5(7)
    assert not is_multiple_of_3_or_5(1)

def test_sample_limit_10():
    """
    For limit 10, numbers: 3, 5, 6, 9 (and 0, but not less than 1).
    Sum should be 3 + 5 + 6 + 9 = 23.
    """
    result = solve(10)
    assert result == 23

def test_project_euler_answer():
    """
    Project Euler official answer for limit 1000.
    """
    expected_answer = 233168
    assert solve(1000) == expected_answer

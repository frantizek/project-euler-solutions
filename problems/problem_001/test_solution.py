"""
Tests for Project Euler Problem 1.
"""
import pytest
from solution import solve

def test_problem_solution():
    """
    Tests that the solution returns the correct answer.
    """
    # Once you know the correct answer, put it here.
    # This ensures that future code changes don't break the solution.
    expected_answer = 233168 # <-- CHANGE THIS LINE
    assert solve() == expected_answer
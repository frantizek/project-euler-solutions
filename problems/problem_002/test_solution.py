"""
Tests for Project Euler Problem 2.
"""
import pytest
from solution import solve

def test_problem_solution():
    """
    Tests that the solution returns the correct answer.
    """
    # Once you know the correct answer, put it here.
    # This ensures that future code changes don't break the solution.
    expected_answer = 4613732 
    assert solve() == expected_answer
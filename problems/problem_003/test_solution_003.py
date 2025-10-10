"""
Tests for Project Euler Problem 3.
"""
import pytest
from solution_003 import solve

def test_problem_solution():
    """
    Tests that the solution returns the correct answer.
    """
    expected_answer = 0 # TODO: Replace with the actual correct answer (6857)
    assert solve() == expected_answer

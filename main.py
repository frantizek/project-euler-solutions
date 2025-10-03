import os
from pathlib import Path

# --- Data for the first 20 problems ---
PROBLEM_DATA = {
    1: "Multiples of 3 or 5",
    2: "Even Fibonacci numbers",
    3: "Largest prime factor",
    4: "Largest palindrome product",
    5: "Smallest multiple",
    6: "Sum square difference",
    7: "10001st prime",
    8: "Largest product in a series",
    9: "Special Pythagorean triplet",
    10: "Summation of primes",
    11: "Largest product in a grid",
    12: "Highly divisible triangular number",
    13: "Large sum",
    14: "Longest Collatz sequence",
    15: "Lattice paths",
    16: "Power digit sum",
    17: "Number letter counts",
    18: "Maximum path sum I",
    19: "Counting Sundays",
    20: "Factorial digit sum",
}

# --- File Templates ---

# Using .format() to avoid conflicts with f-string's curly braces
README_TEMPLATE = """
# Problem {problem_number}: {problem_title}

> [Link to the problem on Project Euler](https://projecteuler.net/problem={problem_number})

## Problem Statement

*(Copy and paste the full problem statement from the Project Euler website here.)*

## My Approach

*(Briefly describe the logic you used to solve the problem.)*

### Final Answer

The final answer is: `[YOUR_ANSWER_HERE]`
""".strip()

SOLUTION_TEMPLATE = """
\"\"\"
Solution for Project Euler Problem {problem_number}: {problem_title}
https://projecteuler.net/problem={problem_number}
\"\"\"

def solve():
    \"\"\"
    Calculates the solution to the problem.
    \"\"\"
    # Your logic goes here
    answer = 0
    return answer

if __name__ == "__main__":
    solution = solve()
    print(f"The solution for problem {problem_number} is: {{solution}}")

""".strip()

TEST_TEMPLATE = """
\"\"\"
Tests for Project Euler Problem {problem_number}.
\"\"\"
import pytest
from solution import solve

def test_problem_solution():
    \"\"\"
    Tests that the solution returns the correct answer.
    \"\"\"
    # Once you know the correct answer, put it here.
    # This ensures that future code changes don't break the solution.
    expected_answer = 0 # TODO: Replace with the actual correct answer
    assert solve() == expected_answer
""".strip()


def create_problem_structure(problem_number: int):
    """
    Generates the directory and template files for a given problem number.
    """
    # Format number with leading zeros (e.g., 1 -> 001, 12 -> 012)
    formatted_number = f"{problem_number:03d}"
    problem_title = PROBLEM_DATA.get(problem_number, "Unknown Title")

    # Define paths
    base_dir = Path("problems")
    problem_dir = base_dir / f"problem_{formatted_number}"

    # Check if directory already exists
    if problem_dir.exists():
        print(f"❌ Directory '{problem_dir}' already exists. Skipping.")
        return

    # Create directory
    print(f"Creating directory: '{problem_dir}'...")
    problem_dir.mkdir(parents=True, exist_ok=True)

    # Create files
    files_to_create = {
        "README.md": README_TEMPLATE.format(problem_number=problem_number, problem_title=problem_title),
        "solution.py": SOLUTION_TEMPLATE.format(problem_number=problem_number, problem_title=problem_title),
        "test_solution.py": TEST_TEMPLATE.format(problem_number=problem_number),
    }

    for filename, content in files_to_create.items():
        file_path = problem_dir / filename
        file_path.write_text(content)
        print(f"   -> Created file: '{file_path}'")

    print(f"\n✅ Successfully created structure for Problem {problem_number}: {problem_title}")


def main():
    """Main function to run the script."""
    print("--- Project Euler Structure Generator ---")
    while True:
        try:
            user_input = input("Enter problem number (e.g., '1', '15') or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Exiting.")
                break

            problem_num = int(user_input)
            if problem_num <= 0:
                print("❌ Please enter a positive number.")
                continue

            create_problem_structure(problem_num)

        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


if __name__ == "__main__":
    main()
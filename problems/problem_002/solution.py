"""
Solution for Project Euler Problem 2: Even Fibonacci numbers
https://projecteuler.net/problem=2
"""

def fibonacci_generator():
    """
    A generator function to yield the next Fibonacci number indefinitely.
    """
    a, b = 1, 2  # Initialize the first two Fibonacci numbers
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to the next Fibonacci numbers

def solve():
    """
    Calculates the solution to the problem.
    """
    fib_gen = fibonacci_generator()

    answer = 0

    current_fibonacci_number = next(fib_gen)

    while current_fibonacci_number < 4000000:
        if current_fibonacci_number % 2 == 0:
            answer += current_fibonacci_number
        current_fibonacci_number = next(fib_gen)

    return answer

if __name__ == "__main__":
    solution = solve()
    print(f"The solution for problem 2 is: {solution}")
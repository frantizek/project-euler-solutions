"""
Solution for Project Euler Problem 1: Multiples of 3 or 5
https://projecteuler.net/problem=1
"""

def solve():
    """
    Calculates the solution to the problem.
    """
    # Your logic goes here
    answer = 0
    for number in range(1, 1000):
        #print(f" -> {number} answer = {answer}")
        if number % 3 == 0 or number % 5 == 0:
            answer += number
    return answer

if __name__ == "__main__":
    solution = solve()
    print(f"The solution for problem 1 is: {solution}")
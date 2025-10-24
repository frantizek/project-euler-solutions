# Problem 3: Largest prime factor

> [Project Euler Problem Statement](https://projecteuler.net/problem=3)

## Problem Statement

The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?

---

## Plan & Approach

**Analysis:**
- Factor the number from the smallest upwards, dividing by each prime/candidate until the remainder is prime.
- Use an efficient primality test for candidates if needed.

**Optimizations:**
- Only check factors up to √n.
- After the loop, if remainder > 1, it's the largest prime factor.

**Edge Cases:**
- n is prime
- n is a product of powers of the same prime

## Running the Code

```commandline
python solution_003.py # Solves the problem
pytest test_solution_003.py # Runs all tests
```


---

## Final Answer

- The final answer for 600851475143 is: **6857**

# Problem 1: Multiples of 3 or 5

> [Project Euler Problem Statement](https://projecteuler.net/problem=1)

## Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

---

## Plan & Approach

**Analysis:**  
- Iterate through numbers from 1 to limit (default 1000).
- Add each number to sum if it's a multiple of 3 or 5.

**Optimization:**  
- (Optional) Use formula for arithmetic progression to compute sum without a loop.

**Edge Cases:**  
- Lower bounds, e.g., limit < 3.
- Limit = 0.
- Large limits.

## Running the Code

```commandline
python solution_001.py # solves for default limit (1000)
pytest test_solution_001.py # runs all tests
```

---

## Final Answer

- The final answer for limit=1000 is: **233168**
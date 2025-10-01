# Problem 1: Multiples of 3 or 5

> [Link to the problem on Project Euler](https://projecteuler.net/problem=1)

## Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## My Approach

This solution uses a simple brute-force method. It iterates through every number from 1 up to (but not including) 1000. For each number, it checks if it's divisible by 3 or 5 using the modulo operator (`%`). If the condition is true, the number is added to a running total.

### Final Answer

The final answer is: `233168`
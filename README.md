# Project Euler Solutions

This repository contains my personal solutions to the problems from [Project Euler](https://projecteuler.net/).

Each problem is solved in Python and contained within its own directory under `/problems`.

## Structure

Each problem directory (`/problems/problem_XXX`) includes:
- `solution.py`: The Python script that calculates the answer.
- `README.md`: The original problem statement and my notes on the approach.

## Setup

This project uses `uv` for package management.

1. Create the virtual environment: `uv venv`
2. Activate the environment: `source .venv/bin/activate`
3. Install dependencies: `uv pip install -e .[dev]`
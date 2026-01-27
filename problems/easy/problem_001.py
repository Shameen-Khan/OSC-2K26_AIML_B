"""
Problem 1: Simple Calculator
Error Type: SYNTAX

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Easy
"""


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return "Unknown operation"

result = calculate(5, 3, '+')
print(result)
"""
Problem 15: Missing function parameter
Error Type: SYNTAX

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Calculate factorial
# Expected Output: Factorial of 5 is 120

def factorial():
    if n <= 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(f"Factorial of 5 is {result}")

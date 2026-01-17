"""
Problem 33: Incorrect indentation
Error Type: SYNTAX

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Calculate the sum of numbers from 1 to n
# Expected Output: Sum of 1 to 5 = 15

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
    total += i
    return total

result = calculate_sum(5)
print(f"Sum of 1 to 5 = {result}")

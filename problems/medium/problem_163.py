"""
Problem 163: List slicing boundary error
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Get last 3 elements of a list
# Expected Output: [30, 40, 50]

numbers = [10, 20, 30, 40, 50]
last_three = numbers[-3:]
print(last_three)
# But what about getting first 3?
first_three = numbers[:3]
print(first_three)  # This works, but is the slice correct for last_three?

"""
Problem 137: Tuple unpacking with wrong count
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Swap three variables using tuple unpacking
# Expected Output: x=3, y=1, z=2

x, y, z = 1, 2, 3
x, y = y, z, x
print(f"x={x}, y={y}, z={z}")

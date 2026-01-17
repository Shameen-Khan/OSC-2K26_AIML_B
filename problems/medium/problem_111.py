"""
Problem 111: List comprehension with wrong variable scope
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Create a list of even squares from 1 to 10
# Expected Output: [4, 16, 36, 64, 100]

numbers = [x ** 2 for x in range(1, 11) if x % 2 == 0]
result = [n for n in numbers if n % 2 == 0]
print(result)

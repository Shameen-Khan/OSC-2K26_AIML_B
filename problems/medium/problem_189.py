"""
Problem 189: Modifying list while iterating
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Remove all negative numbers from list
# Expected Output: [1, 2, 3, 4, 5]

numbers = [-1, 1, -2, 2, -3, 3, 4, -4, 5]
for num in numbers:
    if num < 0:
        numbers.remove(num)
print(numbers)

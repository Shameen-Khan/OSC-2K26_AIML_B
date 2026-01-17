"""
Problem 146: Dictionary modification during iteration
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Remove all items with value less than 5
# Expected Output: {'c': 5, 'd': 10}

data = {'a': 1, 'b': 3, 'c': 5, 'd': 10}
for key in data:
    if data[key] < 5:
        del data[key]
print(data)

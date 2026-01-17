"""
Problem 168: List append vs extend confusion
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Combine multiple lists into one flat list
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [1, 2, 3]
result.append([4, 5, 6])
result.append([7, 8, 9])
print(result)

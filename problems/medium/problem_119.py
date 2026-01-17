"""
Problem 119: Set operations with wrong method
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Find common elements between two lists
# Expected Output: [3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1).union(set(list2)))
print(sorted(common))

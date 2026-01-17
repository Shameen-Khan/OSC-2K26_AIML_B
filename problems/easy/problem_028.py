"""
Problem 28: Wrong boolean operator
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Check if number is between 10 and 20
# Expected Output: True for numbers between 10 and 20

def is_in_range(num):
    return num >= 10 or num <= 20

print(is_in_range(5))  # Should be False
print(is_in_range(15))  # Should be True

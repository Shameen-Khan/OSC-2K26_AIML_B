"""
Problem 147: Incorrect boolean logic with not operator
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Check if a number is NOT in the range 10-20
# Expected Output: True for numbers outside 10-20, False for numbers inside

def not_in_range(num):
    return not num >= 10 and num <= 20

print(not_in_range(5))   # Should be True
print(not_in_range(15))  # Should be False
print(not_in_range(25))  # Should be True

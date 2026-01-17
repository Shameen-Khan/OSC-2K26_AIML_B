"""
Problem 6: Wrong comparison operator
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Check if a number is greater than 10
# Expected Output: True for numbers > 10, False otherwise

def is_greater_than_ten(num):
    return num > 10

result = is_greater_than_ten(5)
print(result)  # Should print False but logic might be wrong

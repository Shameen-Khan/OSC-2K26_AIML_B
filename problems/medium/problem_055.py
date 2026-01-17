"""
Problem 55: Incorrect use of is vs ==
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Check if two numbers are equal
# Expected Output: True for equal numbers

def are_equal(a, b):
    return a is b

print(are_equal(1000, 1000))  # Should print True
print(are_equal(5, 5))

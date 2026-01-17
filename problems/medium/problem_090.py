"""
Problem 90: String formatting with wrong placeholder count
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Format a complete address
# Expected Output: Name: Alice, Age: 25, City: Boston

name = "Alice"
age = 25
city = "Boston"
result = "Name: {}, Age: {}, City: {}".format(name, age)
print(result)

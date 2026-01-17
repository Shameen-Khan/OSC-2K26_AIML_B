"""
Problem 16: Missing colon after if statement
Error Type: SYNTAX

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Calculate if a number is even or odd
# Expected Output: "Even" for even numbers, "Odd" for odd numbers

def check_even_odd(number)
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(10)
print(result)

"""
Problem 53: Integer division causing precision loss
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Calculate average with precision
# Expected Output: Average: 7.5

numbers = [5, 10, 15, 20, 30, 50]
total = sum(numbers)
count = len(numbers)
average = total // count
print(f"Average: {average}")

"""
Problem 25: Division by zero error
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Calculate average of numbers
# Expected Output: Average should be calculated correctly

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

result = calculate_average([])
print(f"Average: {result}")

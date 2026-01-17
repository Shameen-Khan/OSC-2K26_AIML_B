"""
Problem 136: Lambda function with late binding
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Create functions that multiply by 1, 2, 3
# Expected Output: [10, 20, 30]

multipliers = []
for i in [1, 2, 3]:
    multipliers.append(lambda x: x * i)

results = [func(10) for func in multipliers]
print(results)

"""
Problem 243: Monkey patching with method binding
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Dynamically add methods to class instances
# Expected Output: Method should work with correct self binding

class Calculator:
    def __init__(self, value):
        self.value = value

def add(self, x):
    return self.value + x

def multiply(self, x):
    return self.value * x

# Add methods dynamically - but binding is wrong
calc = Calculator(10)
calc.add = add
calc.multiply = multiply

print(calc.add(5))       # Should be 15
print(calc.multiply(3))  # Should be 30

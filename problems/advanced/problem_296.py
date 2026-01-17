"""
Problem 296: Descriptor protocol with incorrect attribute access
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement a validated attribute descriptor
# Expected Output: Should validate on assignment

class Positive:
    def __init__(self, name):
        self.name = name
        
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)
        
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Account:
    balance = Positive("balance")
    
    def __init__(self, initial_balance):
        self.balance = initial_balance

# Test it - but there's an issue with the implementation
acc = Account(100)
print(acc.balance)
acc.balance = -50  # Should raise error

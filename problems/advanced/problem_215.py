"""
Problem 215: Dynamic class creation with type()
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Create classes dynamically with proper initialization
# Expected Output: Dynamically created class should work like normal class

def create_class(name, base_value):
    def __init__(self, value):
        self.value = value + base_value
    
    def get_value(self):
        return self.value
    
    return type(name, (), {
        '__init__': __init__,
        'get_value': get_value,
        'base': base_value
    })

# Create and use dynamic class - method binding issue?
MyClass = create_class('MyClass', 10)
obj = MyClass(5)
print(obj.get_value())  # Should be 15
print(obj.base)         # Should be 10

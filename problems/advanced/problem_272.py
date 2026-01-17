"""
Problem 272: Abstract base class with protocol implementation
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Define abstract interface with default implementation
# Expected Output: Enforce interface while allowing partial implementation

from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass
    
    def validate(self, data):
        # Default implementation
        return len(data) > 0
    
    def run(self, data):
        if not self.validate(data):
            raise ValueError("Invalid data")
        return self.process(data)

class ConcreteProcessor(DataProcessor):
    # Missing process() implementation but should it fail?
    pass

# This will fail but when?
proc = ConcreteProcessor()
result = proc.run([1, 2, 3])

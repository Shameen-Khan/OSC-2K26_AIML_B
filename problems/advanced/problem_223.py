"""
Problem 223: Property with side effects and caching
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement cached property with proper invalidation
# Expected Output: Should cache result but allow invalidation

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if obj not in self.cache:
            self.cache[obj] = self.func(obj)
        return self.cache[obj]

class DataProcessor:
    def __init__(self, data):
        self._data = data
        
    @CachedProperty
    def processed(self):
        print("Processing data...")
        return [x * 2 for x in self._data]
    
    def update_data(self, new_data):
        self._data = new_data
        # Cache not invalidated!

# Test - cache invalidation issue
proc = DataProcessor([1, 2, 3])
print(proc.processed)
proc.update_data([4, 5, 6])
print(proc.processed)  # Should reflect new data

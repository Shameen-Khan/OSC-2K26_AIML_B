"""
Problem 289: Custom iterator with stateful iteration
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement iterator that can be resumed
# Expected Output: Should maintain state across iterations

class ResumableRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Use it - but multiple iterations have issues
r = ResumableRange(1, 5)
print(list(r))  # [1, 2, 3, 4]
print(list(r))  # Should work but returns []

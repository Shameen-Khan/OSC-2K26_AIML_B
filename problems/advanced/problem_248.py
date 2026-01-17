"""
Problem 248: Context manager with improper cleanup
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement a file lock context manager
# Expected Output: Lock should be acquired and released properly

class FileLock:
    def __init__(self, filename):
        self.filename = filename
        self.lock_file = filename + ".lock"
        
    def __enter__(self):
        import os
        if os.path.exists(self.lock_file):
            raise RuntimeError("Lock already held")
        open(self.lock_file, 'w').close()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        import os
        os.remove(self.lock_file)
        return False

# This looks correct but what if __enter__ fails after creating the lock?
with FileLock("data.txt") as lock:
    print("Lock acquired")

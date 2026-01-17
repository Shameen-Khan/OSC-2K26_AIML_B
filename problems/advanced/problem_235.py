"""
Problem 235: Thread-safe singleton with double-checked locking
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement thread-safe singleton
# Expected Output: Only one instance even with multiple threads

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# This looks thread-safe but has subtle issues
def create_instance():
    return ThreadSafeSingleton()

threads = [threading.Thread(target=create_instance) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

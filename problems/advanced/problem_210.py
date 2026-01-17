"""
Problem 210: Weak reference with callback circular dependency
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Use weak references to avoid memory leaks
# Expected Output: Objects should be garbage collected

import weakref

class Observer:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        
    def observe(self, subject):
        self.subjects.append(weakref.ref(subject, self.on_delete))
        
    def on_delete(self, ref):
        print(f"{self.name}: Subject deleted")
        self.subjects.remove(ref)

class Subject:
    def __init__(self, value):
        self.value = value

# Setup observer - but callback creates circular reference
obs = Observer("Watcher")
subj = Subject(42)
obs.observe(subj)
del subj  # Will it be collected?

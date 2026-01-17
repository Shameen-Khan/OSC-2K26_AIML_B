#!/usr/bin/env python3
"""
Problem Generator Script for Open Source Connect - PyExpo 2026
This script generates 200 medium and 100 advanced Python problems with intentional errors.
"""

import os
import random

# Problem templates for medium level (challenging logical and subtle syntax errors)
MEDIUM_PROBLEMS = [
    {
        "description": "List comprehension with wrong variable scope",
        "code": '''# Problem: Create a list of even squares from 1 to 10
# Expected Output: [4, 16, 36, 64, 100]

numbers = [x ** 2 for x in range(1, 11) if x % 2 == 0]
result = [n for n in numbers if n % 2 == 0]
print(result)
''',
        "error_type": "logical"
    },
    {
        "description": "String immutability issue",
        "code": '''# Problem: Replace first character of a string with uppercase
# Expected Output: Hello

word = "hello"
word[0] = "H"
print(word)
''',
        "error_type": "logical"
    },
    {
        "description": "Integer division causing precision loss",
        "code": '''# Problem: Calculate average with precision
# Expected Output: Average: 7.5

numbers = [5, 10, 15, 20, 30, 50]
total = sum(numbers)
count = len(numbers)
average = total // count
print(f"Average: {average}")
''',
        "error_type": "logical"
    },
    {
        "description": "Modifying list while iterating",
        "code": '''# Problem: Remove all negative numbers from list
# Expected Output: [1, 2, 3, 4, 5]

numbers = [-1, 1, -2, 2, -3, 3, 4, -4, 5]
for num in numbers:
    if num < 0:
        numbers.remove(num)
print(numbers)
''',
        "error_type": "logical"
    },
    {
        "description": "Incorrect use of is vs ==",
        "code": '''# Problem: Check if two numbers are equal
# Expected Output: True for equal numbers

def are_equal(a, b):
    return a is b

print(are_equal(1000, 1000))  # Should print True
print(are_equal(5, 5))
''',
        "error_type": "logical"
    },
    {
        "description": "Dictionary modification during iteration",
        "code": '''# Problem: Remove all items with value less than 5
# Expected Output: {'c': 5, 'd': 10}

data = {'a': 1, 'b': 3, 'c': 5, 'd': 10}
for key in data:
    if data[key] < 5:
        del data[key]
print(data)
''',
        "error_type": "logical"
    },
    {
        "description": "Incorrect boolean logic with not operator",
        "code": '''# Problem: Check if a number is NOT in the range 10-20
# Expected Output: True for numbers outside 10-20, False for numbers inside

def not_in_range(num):
    return not num >= 10 and num <= 20

print(not_in_range(5))   # Should be True
print(not_in_range(15))  # Should be False
print(not_in_range(25))  # Should be True
''',
        "error_type": "logical"
    },
    {
        "description": "List slicing boundary error",
        "code": '''# Problem: Get last 3 elements of a list
# Expected Output: [30, 40, 50]

numbers = [10, 20, 30, 40, 50]
last_three = numbers[-3:]
print(last_three)
# But what about getting first 3?
first_three = numbers[:3]
print(first_three)  # This works, but is the slice correct for last_three?
''',
        "error_type": "logical"
    },
    {
        "description": "Set operations with wrong method",
        "code": '''# Problem: Find common elements between two lists
# Expected Output: [3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1).union(set(list2)))
print(sorted(common))
''',
        "error_type": "logical"
    },
    {
        "description": "String formatting with wrong placeholder count",
        "code": '''# Problem: Format a complete address
# Expected Output: Name: Alice, Age: 25, City: Boston

name = "Alice"
age = 25
city = "Boston"
result = "Name: {}, Age: {}, City: {}".format(name, age)
print(result)
''',
        "error_type": "logical"
    },
    {
        "description": "Lambda function with late binding",
        "code": '''# Problem: Create functions that multiply by 1, 2, 3
# Expected Output: [10, 20, 30]

multipliers = []
for i in [1, 2, 3]:
    multipliers.append(lambda x: x * i)

results = [func(10) for func in multipliers]
print(results)
''',
        "error_type": "logical"
    },
    {
        "description": "Tuple unpacking with wrong count",
        "code": '''# Problem: Swap three variables using tuple unpacking
# Expected Output: x=3, y=1, z=2

x, y, z = 1, 2, 3
x, y = y, z, x
print(f"x={x}, y={y}, z={z}")
''',
        "error_type": "logical"
    },
    {
        "description": "List append vs extend confusion",
        "code": '''# Problem: Combine multiple lists into one flat list
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [1, 2, 3]
result.append([4, 5, 6])
result.append([7, 8, 9])
print(result)
''',
        "error_type": "logical"
    },
    {
        "description": "Default parameter evaluation timing",
        "code": '''# Problem: Generate timestamp for each function call
# Expected Output: Different timestamps for each call

import time

def log_message(msg, timestamp=time.time()):
    return f"{timestamp}: {msg}"

print(log_message("First"))
time.sleep(0.1)
print(log_message("Second"))
time.sleep(0.1)
print(log_message("Third"))
''',
        "error_type": "logical"
    },
    {
        "description": "Dictionary get with mutable default value",
        "code": '''# Problem: Count character frequencies in a string
# Expected Output: Correct frequency count

def count_chars(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

result = count_chars("hello")
print(result)  # This works, but try with edge cases
''',
        "error_type": "logical"
    },
]

# Problem templates for advanced level (very challenging, requires deep understanding)
ADVANCED_PROBLEMS = [
    {
        "description": "Metaclass attribute resolution order",
        "code": '''# Problem: Implement a singleton pattern with metaclass
# Expected Output: Same instance should be returned each time

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # Should be True
print(id(db1), id(db2))  # Should be same
''',
        "error_type": "logical"
    },
    {
        "description": "Decorator with arguments and state",
        "code": '''# Problem: Create a retry decorator with exponential backoff
# Expected Output: Function should retry on failure with increasing delays

import time

def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(2 ** attempt)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

# Test it - but there's a subtle bug with the attempts
result = unreliable_function()
print(result)
''',
        "error_type": "logical"
    },
    {
        "description": "Context manager with improper cleanup",
        "code": '''# Problem: Implement a file lock context manager
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
''',
        "error_type": "logical"
    },
    {
        "description": "Circular reference with __del__",
        "code": '''# Problem: Implement a graph node with proper cleanup
# Expected Output: Nodes should be cleaned up without memory leaks

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
    def add_neighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)
        
    def __del__(self):
        print(f"Deleting node {self.value}")

# Create circular reference
a = Node(1)
b = Node(2)
a.add_neighbor(b)

# Try to delete - but __del__ might not be called
del a
del b
print("Deleted nodes")
''',
        "error_type": "logical"
    },
    {
        "description": "Thread-safe singleton with double-checked locking",
        "code": '''# Problem: Implement thread-safe singleton
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
''',
        "error_type": "logical"
    },
    {
        "description": "Descriptor protocol with incorrect attribute access",
        "code": '''# Problem: Implement a validated attribute descriptor
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
''',
        "error_type": "logical"
    },
    {
        "description": "Async iterator with improper resource management",
        "code": '''# Problem: Implement async file reader
# Expected Output: Should read file asynchronously and close properly

import asyncio

class AsyncFileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        
    async def __aiter__(self):
        self.file = open(self.filename, 'r')
        return self
        
    async def __anext__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopAsyncIteration
        return line.strip()

# This async iterator has issues with cleanup on exceptions
async def read_file():
    async for line in AsyncFileReader("data.txt"):
        print(line)

# asyncio.run(read_file())  # Uncomment to test
''',
        "error_type": "logical"
    },
    {
        "description": "Property with side effects and caching",
        "code": '''# Problem: Implement cached property with proper invalidation
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
''',
        "error_type": "logical"
    },
    {
        "description": "Multiple inheritance with super() ambiguity",
        "code": '''# Problem: Implement diamond inheritance correctly
# Expected Output: All classes should be initialized once

class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()

# MRO is correct but initialization order?
d = D()
print("MRO:", [c.__name__ for c in D.__mro__])
''',
        "error_type": "logical"
    },
    {
        "description": "Weak reference with callback circular dependency",
        "code": '''# Problem: Use weak references to avoid memory leaks
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
''',
        "error_type": "logical"
    },
    {
        "description": "Generator send() with exception handling",
        "code": '''# Problem: Implement coroutine with proper exception handling
# Expected Output: Should handle exceptions sent to generator

def coroutine():
    try:
        while True:
            value = yield
            print(f"Received: {value}")
    except GeneratorExit:
        print("Coroutine closing")
    finally:
        print("Cleanup")

# Use the coroutine - but sending exceptions has issues
coro = coroutine()
coro.send(None)  # Prime it
coro.send(10)
coro.send(20)
coro.throw(ValueError, "Error")  # How to handle this?
coro.close()
''',
        "error_type": "logical"
    },
    {
        "description": "Abstract base class with protocol implementation",
        "code": '''# Problem: Define abstract interface with default implementation
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
''',
        "error_type": "logical"
    },
    {
        "description": "Monkey patching with method binding",
        "code": '''# Problem: Dynamically add methods to class instances
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
''',
        "error_type": "logical"
    },
    {
        "description": "Custom iterator with stateful iteration",
        "code": '''# Problem: Implement iterator that can be resumed
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
''',
        "error_type": "logical"
    },
    {
        "description": "Dynamic class creation with type()",
        "code": '''# Problem: Create classes dynamically with proper initialization
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
''',
        "error_type": "logical"
    },
]


def generate_medium_problems(count=150):
    """Generate medium-level problems with variations."""
    problems = []
    
    for i in range(count):
        # Choose a base problem template
        base = MEDIUM_PROBLEMS[i % len(MEDIUM_PROBLEMS)]
        
        # Create variations
        problem = base.copy()
        
        # Add problem number to description
        problem_num = i + 51  # Start from 51 (after easy problems)
        
        problems.append((problem_num, problem))
    
    return problems


def generate_advanced_problems(count=100):
    """Generate advanced-level problems with variations."""
    problems = []
    
    for i in range(count):
        # Choose a base problem template
        base = ADVANCED_PROBLEMS[i % len(ADVANCED_PROBLEMS)]
        
        problem = base.copy()
        problem_num = i + 201  # Start from 201 (after easy and medium)
        
        problems.append((problem_num, problem))
    
    return problems


def write_problem_file(directory, problem_num, problem):
    """Write a problem to a file."""
    filename = f"problem_{problem_num:03d}.py"
    filepath = os.path.join(directory, filename)
    
    # Determine difficulty based on problem number
    if problem_num <= 50:
        difficulty = "Easy"
    elif problem_num <= 200:
        difficulty = "Medium"
    else:
        difficulty = "Advanced"
    
    header = f'''"""
Problem {problem_num}: {problem['description']}
Error Type: {problem['error_type'].upper()}

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: {difficulty}
"""

'''
    
    with open(filepath, 'w') as f:
        f.write(header)
        f.write(problem['code'])


def main():
    """Generate all problems."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    medium_dir = os.path.join(base_dir, "problems", "medium")
    advanced_dir = os.path.join(base_dir, "problems", "advanced")
    
    # Ensure directories exist
    os.makedirs(medium_dir, exist_ok=True)
    os.makedirs(advanced_dir, exist_ok=True)
    
    # Note: Easy problems (1-50) already exist in problems/easy/
    
    print("Generating Medium Problems (51-200)...")
    medium_problems = generate_medium_problems(150)
    for num, problem in medium_problems:
        write_problem_file(medium_dir, num, problem)
    print(f"✓ Generated {len(medium_problems)} medium problems")
    
    print("\nGenerating Advanced Problems (201-300)...")
    advanced_problems = generate_advanced_problems(100)
    for num, problem in advanced_problems:
        write_problem_file(advanced_dir, num, problem)
    print(f"✓ Generated {len(advanced_problems)} advanced problems")
    
    print("\n✓ All problems generated successfully!")
    print(f"  Easy: 50 problems in problems/easy/ (1-50)")
    print(f"  Medium: {len(medium_problems)} problems in problems/medium/ (51-200)")
    print(f"  Advanced: {len(advanced_problems)} problems in problems/advanced/ (201-300)")
    print(f"  Total: {50 + len(medium_problems) + len(advanced_problems)} problems")


if __name__ == "__main__":
    main()

# Python Debugging Guide

Learn how to debug Python code effectively! 🐍

## 🐛 What is Debugging?

Debugging is the process of finding and fixing errors (bugs) in your code. Every programmer debugs – it's a crucial skill!

## 📝 Types of Errors

### 1. Syntax Errors
These are grammatical mistakes in your code. Python can't even run the code!

**Example:**
```python
# Wrong - Missing colon
if x > 5
    print("Big")

# Correct
if x > 5:
    print("Big")
```

### 2. Runtime Errors
Code starts running but crashes during execution.

**Example:**
```python
# Wrong - Division by zero
result = 10 / 0

# Correct - Check first
if denominator != 0:
    result = 10 / denominator
```

### 3. Logical Errors
Code runs without crashing, but gives wrong results.

**Example:**
```python
# Wrong - Off by one
for i in range(1, 10):  # Only goes to 9
    print(i)

# Correct
for i in range(1, 11):  # Goes to 10
    print(i)
```

## 🔍 Debugging Techniques

### 1. Read Error Messages
Python tells you what's wrong!

```python
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    print(x)
NameError: name 'x' is not defined
```

This tells you:
- **What**: `NameError` - variable doesn't exist
- **Where**: Line 3 in test.py
- **Why**: name 'x' is not defined

### 2. Use Print Statements
Add `print()` to see what's happening:

```python
def calculate_average(numbers):
    print(f"Input: {numbers}")  # Debug print
    total = sum(numbers)
    print(f"Total: {total}")    # Debug print
    count = len(numbers)
    print(f"Count: {count}")    # Debug print
    return total / count
```

### 3. Use Python Debugger (pdb)
```python
import pdb

def problematic_function():
    x = 10
    pdb.set_trace()  # Execution pauses here
    y = x * 2
    return y
```

### 4. Comment Out Code
Isolate the problem:

```python
# Step 1: Comment everything
# result = complex_function()
# process_result(result)
# print(result)

# Step 2: Uncomment line by line to find the bug
result = complex_function()
print("After complex_function")  # Debug
# process_result(result)
# print(result)
```

## 🛠️ Common Python Errors and Fixes

### 1. IndentationError
**Problem:**
```python
def greet():
print("Hello")  # Wrong indentation
```

**Fix:**
```python
def greet():
    print("Hello")  # Correct - 4 spaces
```

### 2. NameError
**Problem:**
```python
print(message)  # Variable doesn't exist
```

**Fix:**
```python
message = "Hello"
print(message)
```

### 3. TypeError
**Problem:**
```python
age = 25
message = "You are " + age + " years old"  # Can't add int to string
```

**Fix:**
```python
age = 25
message = "You are " + str(age) + " years old"
# Or use f-string
message = f"You are {age} years old"
```

### 4. IndexError
**Problem:**
```python
numbers = [1, 2, 3]
print(numbers[3])  # Index out of range (0-indexed)
```

**Fix:**
```python
numbers = [1, 2, 3]
print(numbers[2])  # Correct - last item is at index 2
# Or use negative indexing
print(numbers[-1])  # Last item
```

### 5. KeyError
**Problem:**
```python
person = {"name": "Alice", "age": 25}
print(person["email"])  # Key doesn't exist
```

**Fix:**
```python
person = {"name": "Alice", "age": 25}
# Use .get() for safe access
print(person.get("email", "No email"))
# Or check first
if "email" in person:
    print(person["email"])
```

### 6. AttributeError
**Problem:**
```python
numbers = [1, 2, 3]
numbers.append(4)
numbers.add(5)  # Lists don't have .add() method
```

**Fix:**
```python
numbers = [1, 2, 3]
numbers.append(4)  # Correct for lists
numbers.append(5)
```

## 🎯 Debugging Checklist

When you encounter a bug:

- [ ] **Read the error message carefully**
- [ ] **Identify the line number where error occurs**
- [ ] **Check for common mistakes:**
  - [ ] Missing colons `:` after if/for/while/def
  - [ ] Wrong indentation
  - [ ] Typos in variable names
  - [ ] Missing quotes around strings
  - [ ] Using `=` instead of `==` for comparison
  - [ ] Off-by-one errors in ranges
  - [ ] Division by zero
- [ ] **Test with simple inputs first**
- [ ] **Add print statements to track values**
- [ ] **Read the code line by line**

## 💡 Prevention Tips

### 1. Use Meaningful Variable Names
```python
# Bad
x = 10
y = 5
z = x + y

# Good
width = 10
height = 5
area = width + height
```

### 2. Write Comments
```python
# Calculate the total price including tax
price = 100
tax_rate = 0.15
total = price * (1 + tax_rate)
```

### 3. Test Your Code Frequently
Don't write 100 lines then test. Test every few lines!

### 4. Use Type Hints (Python 3.5+)
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

### 5. Follow Python Style Guide (PEP 8)
- Use 4 spaces for indentation
- Use snake_case for variables
- Use descriptive names

## 🔧 Useful Python Functions for Debugging

```python
# Check variable type
type(variable)

# Check if variable exists
'variable_name' in locals()
'variable_name' in globals()

# Get all attributes of an object
dir(object)

# Get help on a function
help(function_name)

# Check Python version
import sys
print(sys.version)
```

## 📊 Debugging Workflow

```
1. Reproduce the error
   ↓
2. Read error message
   ↓
3. Locate the problem
   ↓
4. Form a hypothesis
   ↓
5. Test the hypothesis
   ↓
6. Fix the code
   ↓
7. Test again
   ↓
8. Success! ✓
```

## 🎓 Practice Makes Perfect

The more you debug, the better you get at:
- Recognizing common patterns
- Reading error messages quickly
- Spotting bugs before running code
- Writing bug-free code from the start

## 📚 Additional Resources

- [Python Error Messages Explained](https://docs.python.org/3/tutorial/errors.html)
- [Python Debugger Documentation](https://docs.python.org/3/library/pdb.html)
- [Real Python - Debugging Guide](https://realpython.com/python-debugging-pdb/)

---

**Remember**: Bugs are not failures – they're learning opportunities! 🚀

Every bug you fix makes you a better programmer!

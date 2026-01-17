# 🐛 Problems Directory

Welcome to the Problems Directory! This folder contains Python programming challenges with intentional errors for you to find and fix.

## 📂 Structure

- **easy/** - 50 problems with simple syntax errors and basic logical errors (perfect for beginners)
- **medium/** - 150 problems with intermediate-level logical errors and Python-specific issues
- **advanced/** - 100 problems with complex logical errors, subtle bugs, and advanced Python concepts

## 🎯 How to Solve Problems

### Step 1: Choose a Problem
Navigate to either the `medium` or `advanced` folder and pick a problem file (e.g., `problem_001.py`).

### Step 2: Read the Description
Each file starts with a comment block that includes:
- Problem description
- Error type (SYNTAX or LOGICAL)
- Expected output
- Instructions

### Step 3: Identify the Error
Look carefully at the code and try to find:
- **Syntax Errors**: Missing colons, incorrect indentation, typos, missing quotes
- **Logical Errors**: Wrong operators, off-by-one errors, type mismatches, algorithm issues

### Step 4: Fix the Error
Make the necessary changes to fix the error(s).

### Step 5: Test Your Solution
Run the Python file to see if it produces the expected output:
```bash
python3 problem_001.py
```

### Step 6: Verify
Make sure:
- The code runs without errors
- The output matches the expected output in the comments
- You understand why the error occurred

## 💡 Tips by Difficulty Level

### Easy Problems 🟢
**Common Errors to Look For:**
- Missing colons (`:`) after `if`, `for`, `while`, `def`, `class`
- Incorrect indentation (Python requires consistent indentation)
- Missing or mismatched parentheses, brackets, or quotes
- Typos in variable names or keywords
- Off-by-one errors in loops
- Wrong comparison operators
- Type mismatches (e.g., adding string + integer)

### Medium Problems 🟡
**Common Errors to Look For:**
- String immutability (can't modify strings in place)
- Using `is` instead of `==` for value comparison
- Modifying lists/dicts while iterating over them
- Lambda function variable binding issues
- Incorrect boolean logic with `not`, `and`, `or`
- Wrong set operations (union vs intersection)
- List append vs extend confusion

### Advanced Problems 🔴
**Common Errors to Look For:**
- Mutable default arguments
- Descriptor protocol issues
- Context manager cleanup problems
- Thread safety issues
- Circular references and memory leaks
- Generator exhaustion
- Class vs instance variable confusion
- Multiple inheritance MRO issues

## 📚 Learning Resources

### Git Commands You'll Use:
```bash
# Check status of your changes
git status

# Stage your fixed file
git add problems/medium/problem_001.py

# Commit your fix
git commit -m "Fix: Resolved syntax error in problem_001"

# Push to your fork
git push origin your-branch-name
```

### Testing Your Code:
```bash
# Run a Python file
python3 filename.py

# Check Python syntax without running
python3 -m py_compile filename.py
```

## 🏆 Challenge Yourself

### For Easy Problems 🟢:
- Try to find and fix the error without running the code first
- Understand *why* the error occurs
- Can you spot the error type just by reading?
- Perfect for learning Git workflow!

### For Medium Problems 🟡:
- Requires understanding of Python data structures
- Think about mutability and references
- Consider how Python evaluates expressions
- Test with different inputs

### For Advanced Problems 🔴:
- May require researching Python internals
- Understanding of OOP, decorators, and meta-programming
- Might need to read Python documentation
- Test edge cases and concurrent scenarios
- These will make you think deeply!

## ❓ Need Help?

If you're stuck:
1. Read the error message carefully (if there is one)
2. Check the expected output in the comments
3. Google the error message or concept you don't understand
4. Ask for help in the repository discussions
5. Review Python documentation

## 🎓 What You'll Learn

By solving these problems, you'll gain experience with:
- Python syntax and common pitfalls
- Debugging techniques
- Reading and understanding error messages
- Git and GitHub workflow
- Code review and collaboration
- Problem-solving skills

---

**Remember**: Every expert programmer started as a beginner. Don't be afraid to make mistakes – that's how we learn!

Good luck and happy debugging! 🚀

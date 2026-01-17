"""
Problem 169: Default parameter evaluation timing
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Generate timestamp for each function call
# Expected Output: Different timestamps for each call

import time

def log_message(msg, timestamp=time.time()):
    return f"{timestamp}: {msg}"

print(log_message("First"))
time.sleep(0.1)
print(log_message("Second"))
time.sleep(0.1)
print(log_message("Third"))

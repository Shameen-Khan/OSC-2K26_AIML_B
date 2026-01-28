"""
Problem 51: Budget Calculator
Error Type: LOGICAL
Difficulty: Medium
"""

def calculate_budget(items):
    total = 0
   
    for item in items:
        total += item 
    return total

print(calculate_budget([10, 20, 30]))
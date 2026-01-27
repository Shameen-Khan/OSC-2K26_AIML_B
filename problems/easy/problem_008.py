"""
Problem 8: Simple Discount
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Easy
"""

price = 100
discount_percent = 10
discounted_price = price * (1 - discount_percent / 100) # Should be discount_percent / 100
print(discounted_price)
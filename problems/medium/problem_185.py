"""
Problem 185: Dictionary get with mutable default value
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Medium
"""

# Problem: Count character frequencies in a string
# Expected Output: Correct frequency count

def count_chars(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

result = count_chars("hello")
print(result)  # This works, but try with edge cases

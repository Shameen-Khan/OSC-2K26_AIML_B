"""
Problem 57: Budget Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_budget(val):
    

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    
    
print(check_budget(20))
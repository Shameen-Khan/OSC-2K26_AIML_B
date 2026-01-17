"""
Problem 264: Circular reference with __del__
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement a graph node with proper cleanup
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

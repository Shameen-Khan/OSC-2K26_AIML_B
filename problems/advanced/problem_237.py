"""
Problem 237: Async iterator with improper resource management
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement async file reader
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

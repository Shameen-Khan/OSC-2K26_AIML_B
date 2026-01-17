"""
Problem 241: Generator send() with exception handling
Error Type: LOGICAL

Instructions:
1. Read the code and comments carefully
2. Identify the error(s)
3. Fix the error(s)
4. Test your solution
5. Ensure the output matches the expected output

Difficulty: Advanced
"""

# Problem: Implement coroutine with proper exception handling
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

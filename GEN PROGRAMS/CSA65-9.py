prompt = """
Write a Python program to find factorial.
Use a loop and handle negative input.
"""

print(prompt)

def factorial(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

n = int(input("Enter number: "))

if n < 0:
    print("Invalid input")
else:
    print("Factorial:", factorial(n))

assert factorial(0) == 1
assert factorial(5) == 120

print("Validation successful")

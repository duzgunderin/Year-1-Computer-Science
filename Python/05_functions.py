# 05 - Functions
# Functions let you organize and reuse code.

# Define a simple function
def greet():
    print("Hello!")

greet()

# Function with a parameter
def greet_person(name):
    print("Hello,", name)

greet_person("Alice")
greet_person("Bob")

# Function with a return value
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)

# Function with a default parameter
def power(base, exponent=2):
    return base ** exponent

print("2^3 =", power(2, 3))
print("4^2 =", power(4))       # uses default exponent

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print("Min:", low, "Max:", high)

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

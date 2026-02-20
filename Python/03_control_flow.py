# 03 - Control Flow
# Make decisions in your program using if, elif, and else.

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Comparison operators
a = 5
b = 10
print(a == b)   # Equal
print(a != b)   # Not equal
print(a < b)    # Less than
print(a > b)    # Greater than
print(a <= b)   # Less than or equal
print(a >= b)   # Greater than or equal

# Logical operators
x = 15
print(x > 10 and x < 20)   # Both conditions must be True
print(x < 5 or x > 10)     # At least one condition must be True
print(not (x == 15))        # Reverses the result

# Nested if
number = 7
if number > 0:
    if number % 2 == 0:
        print(number, "is a positive even number")
    else:
        print(number, "is a positive odd number")
else:
    print(number, "is not positive")

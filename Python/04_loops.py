# 04 - Loops
# Repeat actions using for and while loops.

# --- for loop ---
# Loop over a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- while loop ---
count = 0
print("\nCounting up with while:")
while count < 5:
    print(count)
    count += 1

# --- break and continue ---
print("\nSkip 3, stop at 7:")
for n in range(10):
    if n == 3:
        continue    # skip this iteration
    if n == 7:
        break       # exit the loop
    print(n)

# --- Nested loops ---
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

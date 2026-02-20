# 06 - Lists
# Lists store multiple items in a single variable.

# Create a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("List:", numbers)

# Access items by index (starts at 0)
print("First item:", numbers[0])
print("Last item:", numbers[-1])

# Slicing
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])

# Common list operations
numbers.append(7)           # add to end
print("After append:", numbers)

numbers.insert(0, 0)        # insert at position
print("After insert:", numbers)

numbers.remove(1)           # remove first occurrence
print("After remove:", numbers)

popped = numbers.pop()      # remove and return last item
print("Popped:", popped, "| List:", numbers)

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))

# Sorting
numbers.sort()
print("Sorted:", numbers)

numbers.sort(reverse=True)
print("Reverse sorted:", numbers)

# Check membership
print(5 in numbers)
print(99 in numbers)

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# 07 - Dictionaries
# Dictionaries store key-value pairs.

# Create a dictionary
person = {
    "name": "Alice",
    "age": 20,
    "city": "London"
}
print("Dictionary:", person)

# Access values by key
print("Name:", person["name"])
print("Age:", person.get("age"))

# Add or update a key
person["email"] = "alice@example.com"
person["age"] = 21
print("Updated:", person)

# Remove a key
del person["city"]
print("After delete:", person)

# Check if a key exists
print("name" in person)
print("city" in person)

# Loop over a dictionary
print("\nKeys:")
for key in person:
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nKey-value pairs:")
for key, value in person.items():
    print(key, "->", value)

# Nested dictionary
students = {
    "s1": {"name": "Bob", "grade": "A"},
    "s2": {"name": "Carol", "grade": "B"},
}
print("\nStudent s1:", students["s1"]["name"], "-", students["s1"]["grade"])

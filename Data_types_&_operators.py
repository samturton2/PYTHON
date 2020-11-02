# What are data types and operators

# Boolean gives us the outcome in True or False
a = True
b = False

print(a == b)
print(a != b)
print(a >= b)

greetings = "Hello World!"

print(greetings.isalpha())
# Checks if all characters in our string are letters

# Check if the string is lowercase
print(greetings.islower())

print(greetings.startswith("H"))
# checking if string starts with the exact same as your input

print(greetings.endswith("!"))

print(bool(None))
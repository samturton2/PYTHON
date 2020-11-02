# What is concatenation

first_name = "James"
middle_name = "Bond"
last_name = "007"
age = 18
# We want James Bond 007
print(first_name, middle_name, last_name)

# error if you concatenate int with string
# print(age + last_name)

# Casting is used to cast int to string and vice versa
print(str(age) + last_name)
print(int(last_name))

name = input("Please enter your name\n=>")
print("Hello " + name)

# Variables_task update
# Get user data
# Display message your age is +
# Address - including postcode and first line of address - House number
# DOB

# Declaring strings with double and single quotes
# "" as well as ''
single_quotes = 'Single quotes \'wow\''
print(single_quotes)
double_quotes = "double quotes 'wow'"
print(double_quotes)

# String Slicing - why -
# Indexing starts from 0
greetings = "Hello World!"
print(greetings[:5])
# Can do negative indexing
print(greetings[-6:])
# Len returns the length of string variable
print(len(greetings))

white_spaces = "lot's of spaces at the end              "
print(len(white_spaces))
# Delete the white spaces at the end of the string
print(len(white_spaces.strip()))

# count() method counts the number a given word occurs in a string
example_text = "lot's of text with some text"
print(example_text.count('text'))
# Temporary replace "test" with "words"
print(example_text.replace("text", "words"))

print(example_text.capitalize())
print(example_text.upper())
print(example_text.lower())

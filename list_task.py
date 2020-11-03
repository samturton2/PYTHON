# list created with mixed data types
mixed_list = [1, "cat", 54, True, "dog", [1, 2], "bat"]

# create a for loop to go through each item in the list and print its data type
for item in mixed_list:
    print(type(item))

# Add a value at the end of the list
mixed_list.append("rat")
# Delete "dog" from list
mixed_list.remove("dog")
# Replace True with False
mixed_list[3] = False
# Pop "rat" from the end of the list
mixed_list.pop()

# check list now looks like [1, "cat", 54, False, [1, 2], "bat"
print(mixed_list)

# print the list in reverse by starting at the start and print in steps of -1
print(mixed_list[::-1])
# Take the users name, Date of Birth and age
# Print out the inputted data along with the datatype
name = input('Please type your name: ')
print(f'{name} datatype: {type(name)}')

dob = input('Please type your Date of birth (dd/mm/yyyy): ')
print(f'{dob} datatype: {type(dob)}')

age = input('Please type your age: ')
print(f'{age} datatype: {type(age)}')

address = input("Please type your address (House_number Street_name Post_code)\n=> ")
print("Your age is: " + age + "\nYour address is: " + address + "\nYour date of birth is: " + dob)

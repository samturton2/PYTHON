# What is a Dictionary?
# Dictionary (arrays) is another way managing data but more dinamically
# key value pairs to store and manage data
# syntax: {key1: value1, key2: value2, key3: value3}
# what type of data can we store/manage
# Let's create one

devops_student = {
    "key": "value",
    "name": "james",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["operators", "data types", "variables", "sql"],
    "Hobbies": ["watching movies", "rugby", "snowboarding"]
}

print(type(devops_student))

# display the data by fetching the key name

print(devops_student["completed_lessons"])
print(devops_student["completed_lesson_names"])
print(devops_student.keys())

# How can we fetch the value called "data types"
print(devops_student["completed_lesson_names"][1])

# How can i change the value of specific key
devops_student["completed_lessons"] = 3
print(devops_student["completed_lessons"])
print(type(devops_student.items()))

#Task
# create a New dictionary to store user details

# all the details that you utilised in the last task name, DOB, Address, course, grades,
# methods of dictionary to remove, add, replace, display the type of items
# create a list of hobbies of at least 3 items
# display data in reverse order of hobby list

devops_student["Hobbies"].append("running")
print(devops_student)

devops_student["Hobbies"].remove("running")
print(devops_student)
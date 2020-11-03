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
    "completed_lesson_names": ["operators", "data types", "variables", "sql"]
}

print(type(devops_student))

# display the data by fetching the key name

print(devops_student["completed_lessons"])
print(devops_student["completed_lesson_names"])
print(devops_student.keys())

# How can we fetch the value called "data types"
print(devops_student["completed_lesson_names"][1])
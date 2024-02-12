courses = ["MIT", "Cyber security", "Datascience"]
print(courses)

# Accessing an element in array
print(courses[1])

# Looping through an array
for course in courses:
    print(course)

# Adding an element into an array
courses.append("Android Development")
print(courses)

# Deleting and element from an array
courses.remove("Datascience")
print(courses)
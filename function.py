# Inbuilt functions
number = max(89, 70, 23, 54, 100)
print(number)

x = min(66, 45, 88, 23, 8)
print(x)

z = pow(2, 3)
print(z)

# User-defined function
def name():
    print("Maureen")

name() # Calling a function

def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)

student()

# Parameters/Variable and arguments/values
def students(name, age, course):
    print(name, age, course)

students("vincent", 18, "MIT")
students("Grace", 17, "Cyber security")
students("Maureen", 18, "Android programming")
students("Tatiana", 19, "Python")
students("Blessings", 17, "MIT")


# Create a user-defined functions called employees Display;
# 5 employees; fullname, age, gender, position, salary

def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)

employees("Tatiana", 33, "Female", "CEO", 700000)
employees("Tatiana", 33, "Female", "CEO", 700000)
employees("Tatiana", 33, "Female", "CEO", 700000)
employees("Tatiana", 33, "Female", "CEO", 700000)
employees("Tatiana", 33, "Female", "CEO", 700000)



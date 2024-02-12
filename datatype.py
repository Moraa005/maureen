# Data Types
number = 45 # int
num = 56.78 # float
greeting = "Hello there" # str
isPythonInteresting = True # bool

# Variable storing multiple values
languages = ["python", "php", "java"] # list
fruits = ("apple", "banana", "pineapple") # Tuple
countries = {"kenya", "china", "USA"} # set

# Dictionary
details = {
    "firstname" : "Grace",
    "age" : 17,
    "course" : "MIT",
    "nationality" : "North America"
}
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details[ "course"])

# Determining the datatype
print(type(details))
print(type(countries))

# Type casting - converting one datatype to another
print(int(num))
print(float(number))
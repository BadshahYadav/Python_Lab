# Q7.) Write a Python Program toCreate Tuple with different Datatypes. 

# Creating a tuple with different data types
my_tuple = (42, 3.14, "Hello", True, [1, 2, 3], {'key': 'value'}, (4, 5))

# Output the tuple
print("Tuple with different data types:", my_tuple)

# Checking the types of each element in the tuple
for element in my_tuple:
    print(f"Element: {element}, Type: {type(element)}")

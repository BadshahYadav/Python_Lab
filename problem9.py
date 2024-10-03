# Q9.) Write a Python Program to Revers Order. Ex:- “1234abcd” String “dcba4321”output 

# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Input string
input_string = "1234abcd"

# Get the reversed string
reversed_string = reverse_string(input_string)

# Output the reversed string
print("Original string:", input_string)
print("Reversed string:", reversed_string)

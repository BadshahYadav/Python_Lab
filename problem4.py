# Q4.) write a program in python to reverse the digit of the all number in a list

# Function to reverse the digits of a number
def reverse_number(n):
    reversed_num = int(str(n)[::-1]) if n >= 0 else -int(str(n)[:0:-1])
    return reversed_num

# Function to reverse digits of all numbers in a list
def reverse_digits_in_list(numbers):
    return [reverse_number(num) for num in numbers]

# Sample list of numbers
numbers = [123, -456, 7890, -321]

# Reverse the digits of all numbers in the list
reversed_numbers = reverse_digits_in_list(numbers)

# Output the reversed numbers
print("Original list:", numbers)
print("List with reversed digits:", reversed_numbers)

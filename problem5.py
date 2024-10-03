# Q6.) Write a Program int python to create 2 new list odd and even list from the given list

# Function to split numbers into odd and even lists
def split_odd_even(numbers):
    odd_list = [num for num in numbers if num % 2 != 0]
    even_list = [num for num in numbers if num % 2 == 0]
    return odd_list, even_list

# Sample list of numbers
numbers = [10, 21, 4, 45, 66, 93, 11]

# Split the list into odd and even lists
odd_list, even_list = split_odd_even(numbers)

# Output the results
print("Original list:", numbers)
print("Odd numbers list:", odd_list)
print("Even numbers list:", even_list)

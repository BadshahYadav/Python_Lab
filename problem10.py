# Q10.) Write a Python Function that takes two list and return if they have at least one common member.

# Function to check if two lists have at least one common member
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Check for common member
result = have_common_member(list1, list2)

# Output the result
if result:
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")

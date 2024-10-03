# Q11.) Write a python Function called compare which takes two string s1 and s2 and an integer n as arguments. 

# Function to compare the first n characters of two strings
def compare(s1, s2, n):
    # Check if the first n characters of both strings are the same
    if s1[:n] == s2[:n]:
        return True
    else:
        return False

# Example usage
s1 = "hello world"
s2 = "hello python"
n = 5

# Compare the first n characters of s1 and s2
result = compare(s1, s2, n)

# Output the result
if result:
    print(f"The first {n} characters of both strings are the same.")
else:
    print(f"The first {n} characters of both strings are different.")

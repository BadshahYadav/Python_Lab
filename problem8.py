# Q8.) code in python My_list=[‘a’,’b’,’c’,5,6,7,8,9,11,14,’p’,’i’], write a program to print all vowel, consonant and digit are 
# separate and check how many digits are prime, even and odd. 

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in 'aeiou'

# Initialize the list
my_list = ['a', 'b', 'c', 5, 6, 7, 8, 9, 11, 14, 'p', 'i']

# Separate vowels, consonants, and digits
vowels = []
consonants = []
digits = []

for item in my_list:
    if isinstance(item, str):
        if is_vowel(item):
            vowels.append(item)
        else:
            consonants.append(item)
    elif isinstance(item, int):
        digits.append(item)

# Separate the digits into prime, even, and odd
prime_digits = [num for num in digits if is_prime(num)]
even_digits = [num for num in digits if num % 2 == 0]
odd_digits = [num for num in digits if num % 2 != 0]

# Output the results
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Prime digits:", prime_digits)
print("Even digits:", even_digits)
print("Odd digits:", odd_digits)

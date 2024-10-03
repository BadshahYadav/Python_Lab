# Q6.) Write a Program in python to Print list of Alphabet With help of count whether vowel or consonant, if vowel found 
# replace with 8. 

# Function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in 'aeiou'

# Function to process the list of alphabets
def process_alphabets(alphabet_list):
    processed_list = []
    vowel_count = 0
    consonant_count = 0

    for char in alphabet_list:
        if is_vowel(char):
            processed_list.append('8')  # Replace vowel with '8'
            vowel_count += 1
        elif char.isalpha():  # Check if the character is a letter
            processed_list.append(char)
            consonant_count += 1
        else:
            processed_list.append(char)  # For non-alphabet characters

    return processed_list, vowel_count, consonant_count

# Sample list of alphabets
alphabet_list = ['a', 'b', 'c', 'e', 'i', 'o', 'p', 'r', 'u', 'z']

# Process the list
processed_list, vowel_count, consonant_count = process_alphabets(alphabet_list)

# Output the results
print("Original list:", alphabet_list)
print("Processed list:", processed_list)
print("Number of vowels replaced with '8':", vowel_count)
print("Number of consonants:", consonant_count)

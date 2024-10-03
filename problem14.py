# Q14.) Write a Program in python to Display following Output. 
#  SHIFT
#  HIFTS
#  IFTSH
#  FTSHI
#  TSHIF
#  SHIFT 

def display_shifted_words(word):
    # Get the length of the word
    length = len(word)
    
    # Create a list to hold the shifted words
    shifted_words = []
    
    # Loop to create shifted versions of the word
    for i in range(length):
        # Create the shifted word by slicing
        shifted_word = word[i:] + word[:i]
        shifted_words.append(shifted_word)
    
    # Print each shifted word
    for shifted in shifted_words:
        print(shifted)

# Example usage
word = "SHIFT"
display_shifted_words(word)

# Q13.) Write a Program in python to Count the total no of words present in Text file and count the number of “the” present 
# in txt file and Replace it with “THE”.

def process_text_file(file_path):
    # Initialize counters
    total_words = 0
    count_the = 0
    
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Count total words
        words = content.split()
        total_words = len(words)
        
        # Count occurrences of "the"
        count_the = words.count("the")
        
        # Replace "the" with "THE"
        modified_content = content.replace("the", "THE")
        
    # Write the modified content back to the file or to a new file
    with open('modified_' + file_path, 'w') as modified_file:
        modified_file.write(modified_content)
        
    return total_words, count_the

# Example usage
file_path = 'example.txt'  # Replace with your file path
total_words, count_the = process_text_file(file_path)
print(f'Total number of words: {total_words}')
print(f'Number of occurrences of "the": {count_the}')

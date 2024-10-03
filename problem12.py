# Q12.) Write a Python Program to Copy a text file to another file. 

# Function to copy content from one file to another
def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode and destination file in write mode
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                # Read the content from the source file
                content = src.read()
                # Write the content to the destination file
                dest.write(content)
        print(f"Content copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = 'source.txt'       # Specify the source file name
destination_file = 'destination.txt'  # Specify the destination file name

# Call the function to copy the file
copy_file(source_file, destination_file)

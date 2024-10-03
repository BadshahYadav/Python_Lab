# Q3.) write a code in python to print the current date in the following format "Mon May 29 04:51:24 IST 2024"

import time

# Get the current local time
current_time = time.strftime("%a %b %d %H:%M:%S IST %Y")

# Print the formatted time
print(current_time)

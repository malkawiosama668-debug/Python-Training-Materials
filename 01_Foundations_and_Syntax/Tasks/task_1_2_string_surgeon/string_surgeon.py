'''
ask 1.2: The String Surgeon
Objective: Master string immutability, slicing [start:stop:step], and built-in string methods (strip, upper, replace, split).

You have intercepted a messy, unformatted log entry from a legacy database. Your task is to clean and extract the relevant information using Python's string operations.

Where to write your code: Navigate to the task_1_2_string_surgeon directory and write your solution inside the string_surgeon.py file.
Target String: log_entry = "   ERROR-CODE: 404 - file_not_found - admin_node_7   "
Processing Steps:
Clean: Remove the leading and trailing whitespace.
Standardize: Convert the entire cleaned string to uppercase.
Replace: Replace all hyphens (-) with underscores (_).
Extract: Slice the string to extract only the error number (404). Store this in a new variable.
Split: Split the fully cleaned/replaced string into a list of words using the spaces as the delimiter.
Output Requirements: Print the result of each step one by one so you can visually verify how the string transforms through the pipeline.
'''
log_entry = "   ERROR-CODE: 404 - file_not_found - admin_node_7   "


# Remove the gaps at the beginning and end of the string.
Clean=log_entry.strip(" ")
print("log_entry after cleaning:"+ Clean)

# Convert all text to capital letters
Upperize=Clean.upper()
print(("log_entry after Upperized:"+ Upperize))

# Swap line with underline
replacing=Upperize.replace("-","_")
print(("log_entry after replacing:"+ replacing))

# Git the error number
error_number=replacing[12:15]
print("The Error number= "+error_number)

# Convert the text to list
Spliting=replacing.split(" ")
print(("log_entry after Spliting: ",Spliting))

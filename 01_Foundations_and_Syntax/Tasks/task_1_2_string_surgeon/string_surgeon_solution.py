# ==========================================
# Task 1.2: The String Surgeon - Solution
# ==========================================

# The initial messy string
log_entry = "   ERROR-CODE: 404 - file_not_found - admin_node_7   "
print(f"Original String: '{log_entry}'\n")

# 1. Clean: Remove the leading and trailing whitespace
cleaned_log = log_entry.strip()
print("Step 1 (Clean):")
print(cleaned_log)
print("-" * 30)

# 2. Standardize: Convert the entire string to uppercase
upper_log = cleaned_log.upper()
print("Step 2 (Standardize):")
print(upper_log)
print("-" * 30)

# 3. Replace: Replace all hyphens (-) with underscores (_)
replaced_log = upper_log.replace("-", "_")
print("Step 3 (Replace):")
print(replaced_log)
print("-" * 30)

# 4. Extract: Slice the string to extract only the error number (404)
# Counting the index: "ERROR_CODE: " is 12 characters (index 0 to 11).
# The "404" starts at index 12 and ends at index 14, so we slice [12:15]
error_code = replaced_log[12:15]
print("Step 4 (Extract):")
print(error_code)
print("-" * 30)

# 5. Split: Split the fully cleaned/replaced string into a list of words
final_list = replaced_log.split(" ")
print("Step 5 (Split):")
print(final_list)
print("-" * 30)
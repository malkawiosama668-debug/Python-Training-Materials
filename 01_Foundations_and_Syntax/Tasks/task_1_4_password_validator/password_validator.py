'''
Task 1.4: Create an Automated "Password Strength Validator"
Objective: Practice using for and while loops, break and continue keywords, and iterating over strings.

Write a script that checks a user-provided password against complex rules. Use a while loop to keep prompting the user until a valid password is provided.

Where to write your code: Navigate to the task_1_4_password_validator directory and write your solution inside the password_validator.py file.
Rules: The password must meet all the following criteria:
Minimum length of 8 characters.
Contains at least one Uppercase letter.
Contains at least one Lowercase letter.
Contains at least one Digit.
Contains at least one Special Character (!@#$%^&).
Processing: Use a for loop to iterate through the characters of the password and count rule fulfillment. Provide specific feedback to the user on which rules failed. Use the break keyword only when all conditions are met successfully.
'''

password = input("Enter a password to evaluate: ")
    
is_long = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False
has_special = False 
    
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "!@#$%^&":
        has_special = True
            
if is_long and has_upper and has_lower and has_digit and has_special:
    print("Password is valid and accepted!")
else:
    print("Password Invalid. Please fix the following:")
        
    
if not is_long:
    print("Must be at least 8 characters long.")
if not has_upper:
    print("Must contain at least one uppercase letter.")
if not has_lower:
    print("Must contain at least one lowercase letter.")
if not has_digit:
    print("Must contain at least one digit.")
if not has_special:
    print("Must contain at least one special character (!@#$%^&).")
    

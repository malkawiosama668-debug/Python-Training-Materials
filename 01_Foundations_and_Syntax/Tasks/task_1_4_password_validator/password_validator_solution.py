# ==========================================
# Task 1.4: Password Strength Validator
# ==========================================

print("--- Password Strength Validator ---")
print("Rules: Min 8 chars, 1 Upper, 1 Lower, 1 Digit, 1 Special (!@#$%^&)")

# Start an infinite loop that will only end if the password is valid
while True:
    password = input("\nEnter a password to evaluate: ")
    
    # Initialize flags for our rules
    is_long = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Iterate through each character to check conditions
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&":
            has_special = True
            
    # Evaluate the results
    if is_long and has_upper and has_lower and has_digit and has_special:
        print("✅ Password is valid and accepted!")
        break  # Exit the loop successfully
        
    # If we reach here, the password failed at least one rule
    print("❌ Password Invalid. Please fix the following:")
    
    if not is_long:
        print("  - Must be at least 8 characters long.")
    if not has_upper:
        print("  - Must contain at least one uppercase letter.")
    if not has_lower:
        print("  - Must contain at least one lowercase letter.")
    if not has_digit:
        print("  - Must contain at least one digit.")
    if not has_special:
        print("  - Must contain at least one special character (!@#$%^&).")
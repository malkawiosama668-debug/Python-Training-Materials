# user_profile.py

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
weight = float(input("Enter your Weight (in kg): "))
emp_status_str = input("Are you currently employed? (Y/N): ")

# Processing
is_employed = (emp_status_str.strip().upper() == 'Y')
height = 1.75
bmi = weight / (height ** 2)

# Output
print(f"\nProfile for {name}:")
print(f"Age: {age}")
print(f"Weight: {weight} kg")
print(f"Employed: {is_employed}")
print(f"Calculated BMI: {bmi:.2f}")
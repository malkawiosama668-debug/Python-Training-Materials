'''
Task 1.1: Build a Dynamic "User Profile" Generator
Objective: Practice variable assignment, basic data types (string, integer, float, boolean), and using the input() and print() functions.

Create a script that prompts the user for information and prints a formatted summary profile.

Where to write your code: Navigate to the task_1_1_user_profile directory and write your solution inside the user_profile.py file.
Input Requirements: Name (String), Age (Integer), Weight (Float), Employment Status (Boolean: Y/N).
Processing: * Store input in correctly typed variables.
Convert the 'employed' input ('Y'/'N') into a Boolean (True / False).
Calculate BMI using a placeholder height (e.g., 1.75m).
Output: Print a well-formatted summary using f-strings, clearly labeling all gathered and calculated data.
'''
# git person name from user
name=input("enter your name: ")
# git person age from user
age=input("enter your age= ")
# git person weigth from user
Weight=float(input("enter your weigth KG= "))
# git person heigth from user
height=float(input("enter your heigth SM= "))
# git if person is an employee from user 
employment= input("enter if you have job (Y/N): ")

'''
transformation the input to bolyen
if the input is Y will be true 
if not will be false
'''
is_employed = (employment.strip().upper() == 'Y')
'''
calculate the Body Mass Index by
Weight and height
'''
B_M_I=Weight/(height**2)

# Git all of the uotputs 
print(f"Person Name is {name}")
print(f"Person Age is = {age}")
print(f"Person Body Mass Index is = {B_M_I: .2f}")
print(f"is Person Age  = {is_employed}")


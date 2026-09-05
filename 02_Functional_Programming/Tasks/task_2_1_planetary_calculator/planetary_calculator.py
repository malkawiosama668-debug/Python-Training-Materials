"""
Task 2.1: The Planetary Weight Calculator
Objective: Practice defining functions, utilizing positional and keyword arguments, setting default parameters, and managing return values.

Create a modular script that calculates how much an object would weigh on different planets in our solar system.

Where to write your code: Navigate to the task_2_1_planetary_calculator directory and write your solution inside the planetary_calculator.py file.
Requirements:
Define a function named calculate_weight that takes two parameters: mass (in kg) and planet.
Set the planet parameter to have a default value of "Earth".
Inside the function, use conditional logic (if/elif) to multiply the mass by the correct gravity multiplier (Earth = 9.8, Mars = 3.71, Jupiter = 24.79).
The function must return the final calculated weight (do not print it directly inside the function).
Execution: Call your function three times at the bottom of your script and print the results:
Once using only a positional argument for a 100kg mass (relying on the default Earth value).
Once using positional arguments for 100kg on "Mars".
Once using explicit keyword arguments for "Jupiter" and 100kg.
"""

def calculate_weight(mass , planet="Earth"):
    """
    every if will test which planet 
    we are on and multiply the mass with the planet gravity 
    """
    if planet=="Earth":
        return mass*9.8
    elif planet=="Mars":
        return mass*3.71
    elif planet=="Jupiter":
        return mass*24.79

# git the mass with default argument value 
earth_weight=calculate_weight(100)
print(f"Weight on Earth: {earth_weight} N")

mars_weight=calculate_weight(100 , "Mars")
print(f"Weight on MARS: {mars_weight} N")

jupiter_weight=print(calculate_weight(100 , "Jupiter"))
print(f"Weight on jupiter: {jupiter_weight} N")


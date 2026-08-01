# Input/Output (I/O) & String Formatting

In Python, standard Input/Output (I/O) refers to the way a program communicates with the user via the console or terminal. Gathering data from the user and displaying results clearly are fundamental aspects of building interactive applications.

## Standard Input: The input() Function

The `input()` function pauses the execution of your script and waits for the user to type something and press the `Enter` key.

### Basic Usage

You can pass a string argument to input() to serve as a prompt, telling the user what kind of information you expect.

```python
# The script will pause here until the user types their name and presses Enter
username = input("Please enter your username: ")
print("Welcome,", username)
```

### The Golden Rule of `input()`

The `input()` function ALWAYS returns a string (`str`). Even if the user types a number like `42`, Python reads it as the text string `"42"`.

If you want to perform mathematical operations on user input, you must use type casting to convert the string into an integer (`int`) or a float (`float`).

```python
# INCORRECT APPROACH
age = input("Enter your age: ")
# future_age = age + 10  # This will cause a TypeError! Python cannot add a string and an integer.

# CORRECT APPROACH (Type Casting)
age_string = input("Enter your age: ")
age_integer = int(age_string)
future_age = age_integer + 10

# PRO APPROACH (Casting inline)
temperature = float(input("Enter the current temperature: "))
print(temperature + 5.5)
```

## Standard Output: The print() Function

The `print()` function outputs data to the standard output device (usually your screen/console). It converts whatever you pass into it into a string and displays it.

### Basic Printing

You can print variables, direct values, or multiple items separated by commas.

```python
name = "Alice"
age = 28
print("User Profile:")
print(name, age, "Active") # Output: User Profile:\nAlice 28 Active
```

### Advanced `print()` Parameters

By default, `print()` separates multiple items with a space and adds a newline at the end. You can change this behavior using the `sep` and `end` parameters.

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| sep | `" "` (Space) | Dictates what character is printed between multiple arguments. |
| end | `"\n"` (Newline) | Dictates what character is printed at the very end of the output. |

**Code Example:**

```python
# Using the 'sep' parameter to format a date
print(15, 8, 2024, sep="-")  
# Output: 15-8-2024

# Using the 'end' parameter to prevent a new line
print("Loading data", end="... ")
print("Complete!")  
# Output: Loading data... Complete!
```

## String Formatting

When outputting data, you rarely want to print raw variables. You usually want to embed those variables inside a larger, readable sentence. Python provides three main ways to format strings, but f-strings are the modern standard.

### Method 1: F-Strings (Modern Standard)

Introduced in Python 3.6, Formatted String Literals (f-strings) are the fastest, most readable way to format strings. You simply prefix the string with an `f` or `F` and place your variables inside curly braces `{}`.

```Python
user = "Admin"
login_attempts = 3

# F-string approach
print(f"Warning: {user} has failed to log in {login_attempts} times.")
```

**Advanced F-String Features:**

F-strings can also evaluate Python expressions (like math operations or function calls) directly inside the curly braces.

```Python
price = 45.50
tax_rate = 0.08

# Performing math directly inside the f-string
print(f"Subtotal: ${price}")
print(f"Total after tax: ${price + (price * tax_rate)}")

# Formatting numbers (e.g., rounding to 2 decimal places)
print(f"Formatted Total: ${price + (price * tax_rate):.2f}")
```

### Method 2: The `.format()` Method (Legacy 3.x)

Before f-strings, the `.format()` method was the standard. You place empty curly braces `{}` as placeholders in your string, and pass the variables to the `.format()` method at the end. You will often see this in slightly older codebases.

```Python
server = "AWS-US-East"
status = "Online"

# Using positional formatting
print("Server {} is currently {}.".format(server, status))

# Using indexed formatting (useful if repeating variables)
print("Target: {0}. Verifying {0} state... State is {1}.".format(server, status))
```

### Method 3: `%` Formatting (Legacy 2.x)

This is the oldest method, borrowed from the C programming language. It uses the modulo `%` operator to inject variables. While you shouldn't write new code using this method, you might encounter it in very old legacy systems.

```Python
file_name = "data.csv"
size_mb = 14.5

# %s means string, %f means float
print("File %s downloaded. Size: %f MB" % (file_name, size_mb))
```

## Summary Best Practices

1. Always cast your `input()` if you expect a number. Use `int()` for whole numbers and `float()` for decimals.
2. Use F-Strings (`f"..."`) for all your output formatting. They are cleaner, faster, and easier to read than concatenation (`+`) or older formatting methods.
3. Use the `sep` and `end` arguments in `print()` when building complex console outputs (like loading bars or custom data tables).

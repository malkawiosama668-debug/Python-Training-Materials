# Control Flow

By default, a Python script executes sequentially, line by line, from top to bottom. Control Flow refers to the tools and structures that allow you to change this default behavior. By using control flow statements, your program can make decisions, skip certain blocks of code, or choose alternative paths based on dynamic data.

## The `if` Statement

The `if` statement is the most fundamental control flow tool. It evaluates a condition (which must result in a Boolean `True` or `False`). If the condition is `True`, the indented block of code directly beneath it is executed. If it is `False`, the block is skipped.

**Syntax & Example:**

```Python
temperature = 35

if temperature > 30:
    # This block executes because 35 > 30 is True
    print("Warning: High temperature detected!")
    print("Initiating cooling protocols.")

print("System check complete.") # This runs regardless of the condition
```

**Important:** Python uses indentation (standard is 4 spaces) to define code blocks. Forgetting to indent the code inside an `if` statement will result in an `IndentationError`.

## The else Statement

An `if` statement can optionally be followed by an `else` statement. The `else` block serves as a catch-all; it executes only if the preceding `if` condition evaluates to `False`.

**Syntax & Example:**

```Python
battery_level = 15

if battery_level > 20:
    print("Battery level sufficient.")
else:
    # This block executes because the 'if' condition is False
    print("Low battery. Please connect to a power source.")
```

## The `elif` Statement (Else-If)

When you have more than two possible paths, you use `elif` (short for "else if"). You can chain as many `elif` statements as you need. Python evaluates them top-to-bottom and executes only the first block that evaluates to `True`. Once a match is found, the rest of the chain is completely ignored.  

**Syntax & Example:**

```Python
network_status = 403

if network_status == 200:
    print("Connection Successful.")
elif network_status == 404:
    print("Error: Resource Not Found.")
elif network_status == 403:
    # Python stops here and executes this block
    print("Error: Access Forbidden.")
else:
    # The catch-all if none of the above are True
    print("Unknown network status.")
```

## Nested Conditions

You can place an `if` statement inside another `if` statement to check for secondary conditions. This is known as nesting. While powerful, be careful not to nest too deeply, as it makes the code difficult to read.  

**Syntax & Example:**

```Python
user_role = "Admin"
is_logged_in = True

if is_logged_in:
    print("Welcome back!")
    
    # This nested condition only checks if the user is already logged in
    if user_role == "Admin":
        print("Displaying administrator dashboard.")
    else:
        print("Displaying standard user dashboard.")
else:
    print("Please log in to continue.")
```

## Conditional Expressions (The Ternary Operator)

If you have a very simple `if-else` statement that assigns a value to a variable, you can write it in a single line using a conditional expression (often called the ternary operator).

**Format:**
`[value_if_true] if [condition] else [value_if_false]`

**Code Example:**

```Python
# Traditional multi-line approach
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary Operator approach (Clean and Pythonic)
status = "Adult" if age >= 18 else "Minor"

print(f"User classification: {status}")
```

## Structural Pattern Matching (`match` / `case`)

Introduced in Python 3.10

If you are checking a single variable against many possible exact values, you can use the `match` and `case` statements. This is Python's equivalent of the `switch` statement found in other languages like C++ or JavaScript.

**Syntax & Example:**

```Python
command = "start"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "pause":
        print("Engine paused.")
    case _:
        # The underscore (_) acts as the default 'else' catch-all
        print("Unrecognized command.")
```

## Best Practices for Control Flow

1. Avoid deeply nested conditionals: If you find yourself indenting 3 or 4 levels deep, consider combining conditions using logical operators (`and`, `or`) or moving the logic into a separate function.  
2. **Use Truthy and Falsy values:** In Python, empty sequences (like `""` or `[]`), the number `0`, and `None` evaluate to `False`. You can use this for cleaner code.
    * Instead of: `if len(my_list) > 0:`
    * Write: `if my_list:`
3. Order matters: In an `if-elif-else` chain, put your most specific or most likely conditions at the top.

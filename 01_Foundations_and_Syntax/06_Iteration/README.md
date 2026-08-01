# Iteration

Iteration is the process of repeatedly executing a block of code. In Python, this is achieved using loops. Loops allow you to automate repetitive tasks, process collections of data, and manage continuous system states efficiently.

Python provides two primary loop structures: the `while` loop and the `for` loop.  

## The `while` Loop (Condition-Based)

A `while` loop continuously executes its block of code as long as a specified condition remains `True`. It is ideal for situations where you do not know beforehand exactly how many times the loop needs to run (e.g., waiting for user input or monitoring a live sensor).  

**Syntax & Example:**

```Python
# Initializing a control variable
countdown = 5

while countdown > 0:
    print(f"System starting in {countdown}...")
    countdown -= 1  # Decrementing is crucial to avoid an infinite loop

print("System Online!")
```

**Warning: Infinite Loops**
If the condition in a `while` loop never becomes `False`, the loop will run forever. Always ensure that the variables evaluated in the condition are modified within the loop block.

## The `for` Loop (Sequence-Based)

Unlike the `while` loop, Python's `for` loop is a collection-controlled loop. It iterates over the items of any sequence (like a list, tuple, dictionary, set, or string) in the exact order that they appear.  

**Iterating over a List:**

```Python
authorized_users = ["Admin", "System", "Guest"]

for user in authorized_users:
    print(f"Granting access to: {user}")
```

**Iterating over a String:**
Because strings are sequences of characters, you can loop through them directly.

```Python
password = "Secure!"

for character in password:
    print(f"Evaluating character: {character}")
```

## Generating Sequences with `range()`

When you need to execute a block of code a specific number of times, you use the built-in `range()` function in conjunction with a `for` loop.

The `range()` function can take up to three arguments: `range(start, stop, step)`.

* start: The starting integer (default is 0).
* stop: The integer to stop before (it is exclusive).
* step: The increment amount (default is 1).

**Code Examples:**

```Python
# Iterating a specific number of times (0 through 4)
for i in range(5):
    print(f"Attempt {i}")

# Specifying a start and stop (1 through 5)
for i in range(1, 6):
    print(f"Processing batch {i}")

# Specifying a step (counting by 2s)
for i in range(0, 11, 2):
    print(f"Even number: {i}")
```

## Loop Control Statements

Python provides specific keywords to alter the standard flow of a loop dynamically.  

**The `break` Statement**
The `break` keyword immediately terminates the entire loop, regardless of whether the original condition is still true or if there are remaining items in a sequence.  

```Python
target_id = 404
data_stream = [200, 301, 404, 500, 200]

for packet in data_stream:
    if packet == target_id:
        print("Target packet found! Halting search.")
        break  # Exits the loop immediately
    print(f"Scanning packet: {packet}")
```

**The `continue` Statement
The `continue` keyword stops the current iteration and immediately jumps back to the top of the loop to begin the next iteration.  

```Python
server_ports = [22, 80, 443, 8080]

for port in server_ports:
    if port == 80:
        print(f"Skipping unencrypted port {port}.")
        continue  # Skips the rest of the block and moves to 443
    
    print(f"Securing port {port}...")
```

**The `pass` Statement**
The `pass` keyword is a null operation. It does absolutely nothing. It is used as a placeholder when a statement is required syntactically, but you have not yet written the logic.  

```Python
for item in range(10):
    if item % 2 == 0:
        # TODO: Add logic for even numbers later
        pass
    else:
        print(f"Odd number: {item}")
```

## Advanced Feature: The `else` Clause in Loops

Python loops have an optional `else` clause. The code inside the `else` block executes only if the loop completes entirely without encountering a `break` statement.

This is incredibly useful for search algorithms.

```Python
search_item = "Database"
system_modules = ["Network", "Security", "UI"]

for module in system_modules:
    if module == search_item:
        print(f"{search_item} found in system!")
        break
else:
    # This executes because the loop finished naturally (no break occurred)
    print(f"Error: {search_item} module is missing.")
```

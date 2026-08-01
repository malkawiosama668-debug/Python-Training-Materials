# Operators

Operators are special symbols or keywords in Python used to carry out specific calculations, comparisons, or logical operations on variables and values (known as operands).

Understanding how to manipulate data using these operators is a foundational skill in Python programming. Below is a detailed breakdown of the primary operator categories.

## Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations.

| Operator | Name | Description | "Example (a = 10, b = 3)" | Result |
| -------- | ---- | ----------- | ------------------------- | ------ |
| + | Addition | Adds two operands | a + b | 13 |
| - | Subtraction | Subtracts right operand from the left | a - b | 7 |
| * | Multiplication | Multiplies two operands | a * b | 30 |
| / | True Division | Divides left operand by the right (always returns a float) | a / b | 3.3333... |
| // | Floor Division | Divides and rounds down to the nearest whole integer | a // b | 3 |
| % | Modulo | Returns the remainder of the division | a % b | 1 |
| ** | Exponentiation | Raises the left operand to the power of the right | a ** b | 1000 |

**Code Example:**

```python
total_items = 14
box_capacity = 4

# How many full boxes can we pack?
boxes_packed = total_items // box_capacity  # Result: 3

# How many items are left over?
items_left = total_items % box_capacity     # Result: 2
```

## Comparison (Relational) Operators

Comparison operators are used to compare two values. They evaluate the condition and always return a Boolean value (`True` or `False`).

| Operator | Name | Description | "Example (x = 5, y = 8)" | Result |
| -------- | ---- | ----------- | ------------------------- | ------ |
| == | Equal | True if both operands are equal | x == y | False |
| != | Not Equal | True if operands are not equal | x != y | True |
| > | Greater Than | True if left operand is greater than the right | x > y | False |
| < | Less Than | True if left operand is less than the right | x < y | True |
| >= | Greater or Equal | True if left is greater than or equal to the right | x >= y | False |
| <= | Less or Equal | True if left is less than or equal to the right | x <= y | True |

**Code Example:**

```python
sensor_reading = 95.5
threshold = 100.0

if sensor_reading >= threshold:
    print("Warning: Threshold exceeded!")
else:
    print("System operating normally.") # This will execute
```

## Logical Operators

Logical operators are used to combine multiple conditional statements.

| Operator | Description | Example |
| -------- | ----------- | ------- |
| and | Returns True if both statements are true | (5 > 3) and (10 < 20) (True) |
| or | Returns True if at least one statement is true | (5 > 3) or (10 > 20) (True) |
| not | Reverses the logical state of its operand | not (5 > 3) (False) |

**Note on Short-Circuiting:** Python optimizes logical evaluation. In an `and` statement, if the first condition is `False`, Python immediately stops checking the second condition because the overall statement can never be `True`.

**Code Example:**

```python
is_admin = True
is_active = False

# The user must be both an admin AND active to get access
if is_admin and is_active:
    print("Access Granted.")
else:
    print("Access Denied.") # This will execute
```

## Assignment Operators

Assignment operators are used to assign values to variables. Python also supports compound assignment operators, which perform an arithmetic operation and an assignment in a single step.

| Operator | Example | Equivalent To | Description |
| -------- | ------- | ------------- | ----------- |
| = | x = 5 | x = 5 | Assigns the right-side value to the left-side variable. |
| += | x += 3 | x = x + 3 | Adds and assigns. |
| -= | x -= 3 | x = x - 3 | Subtracts and assigns. |
| *= | x *= 3 | x = x * 3 | Multiplies and assigns. |
| /= | x /= 3 | x = x / 3 | Divides and assigns. |
| //= | x //= 3 | x = x // 3 | Floor divides and assigns. |
| %= | x %= 3 | x = x % 3 | Calculates modulo and assigns. |

**Code Example:**

```python
counter = 0
counter += 1  # counter is now 1
counter += 5  # counter is now 6
```

## Identity Operators

Identity operators compare the memory locations of two objects, not their actual values. They are used to determine if two variables point to the exact same object in memory.

| Operator | Description | Example |
| -------- | ----------- | ------- |
| is | Returns True if both variables point to the same object | x is y |
| is not | Returns True if both variables point to different objects | x is not y |

**Code Example:**

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

# Comparing values (==)
print(list_a == list_b)  # True: They contain the exact same numbers.

# Comparing memory identity (is)
print(list_a is list_b)  # False: They are different objects in memory.
print(list_a is list_c)  # True: list_c points to the exact same memory address as list_a.
```

## Membership Operators

Membership operators are incredibly useful in Python for testing whether a specific value or variable is found within a sequence (like a string, list, tuple, or dictionary).

| Operator | Description | Example |
| -------- | ----------- | ------- |
| in | Returns `True` if a sequence with the specified value is present | `"x" in ["x", "y", "z"]` |
| not in | Returns `True` if a sequence with the specified value is NOT present | `"a" not in "hello"` |

**Code Example:**

```python
allowed_users = ["alice", "bob", "charlie"]
current_user = "eve"

if current_user not in allowed_users:
    print("Intruder detected!")
```

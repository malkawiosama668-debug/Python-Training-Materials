# Variables & Data Types: The Memory Foundations of Python

**What is a variable?**
In Python, a variable is not a "box" that stores data. Instead, it is a label or a reference tag attached to an object in memory.

Python is dynamically typed, meaning you do not need to declare a variable's type explicitly before using it. The Python interpreter infers the type at runtime based on the value assigned.

**Example:**
When you type x = 10, Python does three things:

1. Creates an integer object with the value 10 in a private memory space called the Heap.
2. Assigns a unique memory address to that object.
3. Binds the label x to that memory address.

If you then type y = x, Python does not copy the number 10. It simply attaches the label y to the exact same memory address as x. You can verify this using the id() function, which returns an object's memory address.

However, Python is also strongly typed. It will not automatically coerce types in ways that lose data (e.g., it won't silently add a string to an integer without explicit conversion).

## Data Types Overview

Python is dynamically typed; the interpreter infers the type at runtime.

* **Integers (int):** Whole numbers of arbitrary length.
* **Floats (float):** Decimal numbers (IEEE 754 double precision).
* **Strings (str):** Immutable sequences of Unicode characters.
* **Booleans (bool):** Represents truth values (True or False).
  
Example: Defining System States

```python
# Variables representing data from a PV Solar Power Plant inspection
panel_id = "Zone_A_String_14"   # str: Alphanumeric identifier
surface_temp_celsius = 48.5     # float: Continuous decimal measurement
defect_detected = False         # bool: Binary state
packet_transmit_rate = 1024     # int: Discrete count

# Checking types dynamically
print(type(surface_temp_celsius)) # Output: <class 'float'>
```

Type Casting:

Often, you must convert data from one type to another, especially when reading from files or taking user input.

```python
string_temp = "48.5"
actual_temp = float(string_temp) # Casts the string to a usable float
```

## Strings and String Operations

Strings (str) are immutable sequences of Unicode characters. Because they are immutable, any operation that modifies a string actually creates a brand new string in memory.

```Python
text = " Python Training "

# 1. Concatenation and Repetition
greeting = "Hello" + " World"  # Addition combines strings
echo = "Echo! " * 3            # Multiplication repeats them

# 2. Slicing [start:stop:step]
language = text[1:7]           # Extracts "Python"
reversed_text = text[::-1]     # Reverses the string

# 3. Built-in Methods
clean_text = text.strip()              # Removes leading/trailing whitespace
shouted = text.upper()                 # Converts to " PYTHON TRAINING "
word_list = clean_text.split(" ")      # Splits into a list: ['Python', 'Training']
replaced = clean_text.replace("P", "C")# "Cython Training"
```

**Why use each data type and data structure?**

Choosing the right structure is the essence of software engineering.

* Use int for countable, discrete items (loop iterations, array indices).
* Use float for continuous measurements requiring precision (temperature, sensor data, financial calculations).
* Use bool for flags, system states, and conditional triggers (e.g., is_connected = True).
* Use str for textual data, IDs, and human-readable output.

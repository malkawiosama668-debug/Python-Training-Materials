# Variables & Data Types: The Memory Foundations of Python

Python is dynamically typed, meaning you do not need to declare a variable's type explicitly before using it. The Python interpreter infers the type at runtime based on the value assigned.

However, Python is also strongly typed. It will not automatically coerce types in ways that lose data (e.g., it won't silently add a string to an integer without explicit conversion).

Core Primitives:
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


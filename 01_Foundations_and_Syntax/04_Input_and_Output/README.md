# Input/Output (I/O) & String Formatting

Handling data ingress and egress is the first step in building interactive scripts.

## Standard Input:
The `input()` function pauses execution and waits for the user to type something and press Enter. 

Crucial Rule: `input()` always returns a String (str). If you need a number, you must cast it immediately.

```python
# Gathering configuration parameters
target_ip = input("Enter the target IP address: ")
timeout_seconds = int(input("Enter timeout in seconds: ")) # Immediate cast to int
```

## Standard Output & F-Strings:
Introduced in Python 3.6, formatted string literals (f-strings) are the most efficient and readable way to inject variables into strings. Prefix the string with f and place variables inside curly braces {}.

```python
# Standard concatenation (Prone to errors)
print("Scanning " + target_ip + " with a timeout of " + str(timeout_seconds))

# F-String approach (Clean and highly readable)
print(f"Scanning {target_ip} with a timeout of {timeout_seconds} seconds.")
```

## Task from HackerRank:
* **Task 01:** [Say "Hello, World!" With Python](https://www.hackerrank.com/challenges/py-hello-world/problem?isFullScreen=true)
# Module 01: Foundations & Syntax

Welcome to the first module of the Python Training Program. This section covers the fundamental building blocks of Python programming, transitioning from basic variable assignment to complex logical iterations.

## Topics Covered
* **[01. Python Rules & Principles:](./01_Python_Rules_and_Principles/)** Understanding the governing rules and philosophy of Python
* **[02. Variables & Data Types:](./02_Variables_and_Data_Types/)** Understanding primitive data types including Integers, Floats, Strings, and Booleans.
* **[03. Operators:](./03_Operators/)** Undersanding 
* **[04. Input/Output:](./04_Input_and_Output/)** Mastering basic I/O operations using `input()` and `print()`.
* **[05. Control Flow:](./05_Controle_Flow/)** Implementing conditionals utilizing `if`, `elif`, and `else` clauses.
* **[06. Iteration:](./06_Iteration/)** Deep dive into `for` and `while` loops, iterating over sequences, and using control statements like `break`, `continue`, and `pass`.

---

## Hands-On Practice Tasks

To master these concepts, complete the following three tasks. Navigate to the respective sub-directories to write and test your code.

### Task 1.1: Build a Dynamic "User Profile" Generator
**Objective:** Practice variable assignment, basic data types (string, integer, float, boolean), and using the `input()` and `print()` functions.

Create a script that prompts the user for information and prints a formatted summary profile.

* **Input Requirements:** Name (String), Age (Integer), Weight (Float), Employment Status (Boolean: Y/N).
* **Processing:** * Store input in correctly typed variables.
  * Convert the 'employed' input ('Y'/'N') into a Boolean (`True` / `False`).
  * Calculate BMI using a placeholder height (e.g., 1.75m).
* **Output:** Print a well-formatted summary using f-strings, clearly labeling all gathered and calculated data.

---

### Task 1.2: Develop a Comprehensive "Logic Gate Simulator"
**Objective:** Master `if`, `elif`, and `else` statements, and implement logical operators (`and`, `or`, `not`) and nested conditions.

Create a program that simulates fundamental logic gates (AND, OR, NOT, XOR).

* **Input:** Two boolean inputs (A and B, accepted as `True`/`False` or `1`/`0`).
* **Requirements:** * Implement checks for AND, OR, and NOT gates. 
  * Implement an XOR gate using nested logic or combined operators (XOR is True only if A and B differ).
* **User Interaction:** Prompt the user to select a gate to test, take the necessary inputs, and print the resulting output.

---

### Task 1.3: Create an Automated "Password Strength Validator"
**Objective:** Practice using `for` and `while` loops, `break` and `continue` keywords, and iterating over strings.

Write a script that checks a user-provided password against complex rules. Use a `while` loop to keep prompting the user until a valid password is provided.

* **Rules:** The password must meet all the following criteria:
  * Minimum length of 8 characters.
  * Contains at least one Uppercase letter.
  * Contains at least one Lowercase letter.
  * Contains at least one Digit.
  * Contains at least one Special Character (!@#$%^&).
* **Processing:** Use a `for` loop to iterate through the characters of the password and count rule fulfillment. Provide specific feedback to the user on which rules failed. Use the `break` keyword only when all conditions are met successfully.
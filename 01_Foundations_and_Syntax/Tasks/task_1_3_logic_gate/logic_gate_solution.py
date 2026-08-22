# ==========================================
# Task 1.3: Logic Gate Simulator - Solution
# ==========================================

print("--- Logic Gate Simulator ---")
print("Available Gates: AND, OR, NOT, XOR")

# 1. Prompt user for the gate type
gate = input("Select a gate to test: ").strip().upper()

# 2. Get Input A
# We convert the input string "1" or "0" into an integer, then into a boolean
input_a_str = input("Enter input A (1 or 0): ")
val_a = bool(int(input_a_str))

# The NOT gate only takes one input, so we only ask for B if it's NOT the NOT gate.
if gate != "NOT":
    input_b_str = input("Enter input B (1 or 0): ")
    val_b = bool(int(input_b_str))
else:
    val_b = None

print("\n--- Result ---")

# 3. Process the logic based on the chosen gate
if gate == "AND":
    result = val_a and val_b
    print(f"AND Gate Output: {result}")

elif gate == "OR":
    result = val_a or val_b
    print(f"OR Gate Output: {result}")

elif gate == "NOT":
    result = not val_a
    print(f"NOT Gate Output: {result}")

elif gate == "XOR":
    # XOR is True if the values are different
    # This can be written as (val_a and not val_b) or (not val_a and val_b)
    # But a cleaner nested logic approach is simply comparing them:
    result = val_a != val_b
    print(f"XOR Gate Output: {result}")

else:
    print("Error: Unrecognized gate selected.")
# test_logic_gate.py
import subprocess
import sys

def run_test():
    print("Running automated tests for logic_gate.py...\n")

    # Define test cases: (Simulated Input, Expected Output text)
    test_cases = [
        ("AND\n1\n1\n", "True", "AND Gate (1, 1)"),
        ("AND\n1\n0\n", "False", "AND Gate (1, 0)"),
        ("OR\n0\n0\n", "False", "OR Gate (0, 0)"),
        ("OR\n1\n0\n", "True", "OR Gate (1, 0)"),
        ("XOR\n1\n0\n", "True", "XOR Gate (1, 0)"),
        ("XOR\n1\n1\n", "False", "XOR Gate (1, 1)"),
        ("NOT\n0\n", "True", "NOT Gate (0)")
    ]

    all_passed = True

    for user_input, expected_result, test_name in test_cases:
        try:
            process = subprocess.run(
                [sys.executable, "logic_gate.py"],
                input=user_input,
                text=True,
                capture_output=True,
                check=True
            )
            
            output = process.stdout
            
            # Check if the expected boolean result is printed in the output
            if expected_result not in output:
                print(f"❌ {test_name} Failed. Expected result: {expected_result}")
                all_passed = False
            else:
                print(f"✅ {test_name} Passed.")

        except FileNotFoundError:
            print("❌ Error: Could not find 'logic_gate.py'.")
            return
        except subprocess.CalledProcessError as e:
            print(f"❌ Script crashed on test {test_name}.")
            all_passed = False

    if all_passed:
        print("\n🏆 All logic gates are functioning perfectly!")
    else:
        print("\n⚠️ Some tests failed. Please review your logic and try again.")

if __name__ == "__main__":
    run_test()
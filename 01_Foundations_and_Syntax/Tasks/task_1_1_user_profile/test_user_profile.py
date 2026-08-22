# test_user_profile.py
import subprocess
import sys

def run_test():
    print("Running automated test for user_profile.py...")

    # 1. Simulate the user typing these inputs, separated by newlines (Enter keys)
    # Name: Alice, Age: 25, Weight: 68.5, Employed: Y
    simulated_input = "Alice\n25\n68.5\nY\n"

    # 2. Run the student's script using subprocess
    process = subprocess.run(
        [sys.executable, "user_profile.py"],
        input=simulated_input,
        text=True,
        capture_output=True
    )

    # 3. Capture the printed output
    output = process.stdout

    # 4. Define our test assertions
    try:
        assert "Alice" in output, "Test Failed: Name not found in output."
        assert "25" in output, "Test Failed: Age not found in output."
        assert "True" in output, "Test Failed: Employment status not evaluated correctly."
        
        # BMI for 68.5kg at 1.75m is exactly 22.3673... which formats to 22.37
        assert "22.37" in output, "Test Failed: BMI calculation or formatting is incorrect."
        
        print("✅ All tests passed successfully! The logic is sound.")
    
    except AssertionError as e:
        print(f"❌ {e}")
        print("Raw Output from script was:\n", output)

if __name__ == "__main__":
    run_test()
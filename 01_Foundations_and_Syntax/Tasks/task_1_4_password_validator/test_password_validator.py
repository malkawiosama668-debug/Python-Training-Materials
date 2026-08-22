# test_password_validator.py
import subprocess
import sys

def run_test():
    print("Running automated tests for password_validator.py...\n")

    # We simulate a user typing a series of passwords. 
    # The first 5 fail different rules. The final one is valid and should break the loop.
    simulated_inputs = [
        "short",             # Fails length, upper, digit, special
        "noupper1!",         # Fails uppercase
        "NOLOWER1!",         # Fails lowercase
        "NoDigitHere!!",     # Fails digit
        "NoSpecialChar12",   # Fails special character
        "ValidPass123!"      # Passes all
    ]
    
    input_string = "\n".join(simulated_inputs) + "\n"

    try:
        process = subprocess.run(
            [sys.executable, "password_validator.py"],
            input=input_string,
            text=True,
            capture_output=True,
            check=True
        )
        
        output = process.stdout.lower()
        
        # Assertions to check if the program looped and caught the errors
        assert "uppercase" in output, "Test Failed: Did not provide feedback about missing uppercase letters."
        assert "lowercase" in output, "Test Failed: Did not provide feedback about missing lowercase letters."
        assert "digit" in output or "number" in output, "Test Failed: Did not provide feedback about missing digits."
        assert "special" in output or "character" in output, "Test Failed: Did not provide feedback about missing special characters."
        
        # Check if the final success condition was met
        assert "success" in output or "valid" in output or "accepted" in output, "Test Failed: Did not accept the valid password."
        
        print("✅ All tests passed successfully! The validator correctly checks rules and loops.")

    except FileNotFoundError:
        print("❌ Error: Could not find 'password_validator.py'.")
    except subprocess.CalledProcessError as e:
        print("❌ Script crashed. Ensure you are using a while loop that eventually breaks.")
        print("Error details:\n", e.stderr)
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output ---")
        print(process.stdout)

if __name__ == "__main__":
    run_test()
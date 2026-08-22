# test_string_surgeon.py
import subprocess
import sys

def run_test():
    print("Running automated test for string_surgeon.py...\n")

    # 1. Run the student's script using subprocess
    try:
        process = subprocess.run(
            [sys.executable, "string_surgeon.py"],
            text=True,
            capture_output=True,
            check=True
        )
    except FileNotFoundError:
        print("❌ Error: Could not find 'string_surgeon.py'. Make sure you are in the correct directory and the file is named correctly.")
        return
    except subprocess.CalledProcessError as e:
        print("❌ Error: Your script crashed while running. Check your Python code for syntax errors.")
        print("Error details:\n", e.stderr)
        return

    # 2. Capture the printed output
    output = process.stdout
    
    # Define expected transformations
    expected_clean = "ERROR-CODE: 404 - file_not_found - admin_node_7"
    expected_upper = "ERROR-CODE: 404 - FILE_NOT_FOUND - ADMIN_NODE_7"
    expected_replace = "ERROR_CODE: 404 _ FILE_NOT_FOUND _ ADMIN_NODE_7"
    expected_extract = "404"
    
    # The string representation of the final split list
    expected_list = "['ERROR_CODE:', '404', '_', 'FILE_NOT_FOUND', '_', 'ADMIN_NODE_7']"

    # 3. Define our test assertions
    try:
        assert expected_clean in output, "Test Failed (Step 1): Did not find the correctly stripped string."
        assert expected_upper in output, "Test Failed (Step 2): Did not find the correctly uppercased string."
        assert expected_replace in output, "Test Failed (Step 3): Did not find the string with replaced hyphens."
        
        # Check if 404 was printed distinctly 
        # (Looking for it surrounded by newlines or spaces to ensure it was printed as a standalone variable)
        assert expected_extract in output, "Test Failed (Step 4): Did not find the extracted '404' error code."
        
        # Check for the final list structure
        assert expected_list in output.replace('"', "'"), "Test Failed (Step 5): The final split list does not match the expected output. Make sure you are splitting by spaces."
        
        print("✅ All tests passed successfully! You are a master String Surgeon.")
    
    except AssertionError as e:
        print(f"❌ {e}")
        print("\n--- Raw Output from your script was ---")
        print(output if output.strip() else "<No Output Produced>")

if __name__ == "__main__":
    run_test()
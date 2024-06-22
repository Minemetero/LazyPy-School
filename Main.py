"""
Version: beta-0.1
Author: Minemetero
"""
import os

def run_script(script_name):
    try:
        # Execute the selected script
        os.system(f'python {script_name}')
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

def main():
    scripts = {
        "1": "InequalityStatement_Calculator.py",
        "2": "NumberLine_Calculator.py",
        "3": "Triangle_Calculator.py",
        "4": "VelocityDisplacement_Calculator.py"
    }
    
    while True:
        print("\nPlease choose a script to run:")
        for key, value in scripts.items():
            print(f"{key}: {value}")

        choice = input("\nEnter the number of the script you want to run (or 'q' to quit): ")

        if choice == 'q':
            print("Exiting...")
            break
        elif choice in scripts:
            run_script(scripts[choice])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

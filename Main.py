"""
Version: 1.0.1
Author: Minemetero
"""
import os
import subprocess
import sys

def install_packages(packages):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
    except Exception as e:
        print(f"An error occurred while installing packages: {e}")

def run_script(script_name, required_packages):
    # Check for and install any required packages
    if required_packages:
        install_packages(required_packages)
    
    try:
        # Execute the selected script
        os.system(f'python {script_name}')
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

def main():
    scripts = {
        "1": {"name": "InequalityStatement_Calculator","path": "src/InequalityStatement_Calculator.py", "packages": ["sympy"]},
        "2": {"name": "NumberLine_Calculator", "path": "src/NumberLine_Calculator.py","packages": ["matplotlib","numpy"]},
        "3": {"name": "Triangle_Calculator", "path": "src/Triangle_Calculator.py","packages": ["turtle"]},
        "4": {"name": "VelocityDisplacement_Calculator", "path": "src/VelocityDisplacement_Calculator.py","packages": []}
    }
    
    while True:
        print("\nPlease choose a script to run:")
        for key, value in scripts.items():
            print(f"{key}: {value['name']}")

        choice = input("\nEnter the number of the script you want to run (or 'q' to quit): ")

        if choice == 'q':
            print("Exiting...")
            break
        elif choice in scripts:
            run_script(scripts[choice]["path"], scripts[choice]["packages"])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

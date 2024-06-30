"""
Version: 1.1.2
Author: Minemetero
"""
import os
import subprocess
import sys

def install_packages(requirements_file):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    except Exception as e:
        print(f"An error occurred while installing packages: {e}")

def run_script(script_path):
    try:
        # Execute the selected script
        os.system(f'python {script_path}')
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

def main():
    scripts = {
        "1": {"name": "InequalityStatement_Calculator", "path": "src/InequalityStatement_Calculator.py", "requirements": "requirements/InequalityStatement.txt"},
        "2": {"name": "NumberLine_Calculator", "path": "src/NumberLine_Calculator.py", "requirements": "requirements/NumberLine.txt"},
        "3": {"name": "Triangle_Calculator", "path": "src/Triangle_Calculator.py", "requirements": "requirements/Triangle.txt"},
        "4": {"name": "VelocityDisplacement_Calculator", "path": "src/VelocityDisplacement_Calculator.py", "requirements": "requirements/VelocityDisplacement.txt"}
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
            requirements_file = scripts[choice]["requirements"]
            if os.path.exists(requirements_file):
                print(f"Installing packages from {requirements_file}...")
                install_packages(requirements_file)
            else:
                print(f"No requirements file found for {scripts[choice]['name']}.")
            run_script(scripts[choice]["path"])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

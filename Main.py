"""
Version: 1.1.3
Author: Minemetero
"""
import os
import subprocess
import sys

def install_packages(requirements_file):
    if os.path.exists(requirements_file):
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing packages: {e}")
    else:
        print(f"Requirements file '{requirements_file}' not found. Skipping package installation.")

def run_script(script_path):
    try:
        result = subprocess.run([sys.executable, script_path], check=True)
        if result.returncode == 0:
            print(f"Script {script_path} executed successfully.")
        else:
            print(f"Script {script_path} failed with return code {result.returncode}.")
    except subprocess.CalledProcessError as e:
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
            script_info = scripts[choice]
            print(f"Installing packages from {script_info['requirements']}...")
            install_packages(script_info["requirements"])
            print(f"Running script {script_info['path']}...")
            run_script(script_info["path"])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

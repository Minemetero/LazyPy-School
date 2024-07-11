"""
Version: 1.2.0
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

def discover_scripts(script_dir, requirements_dir):
    scripts = {}
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py')]
    
    for index, script_file in enumerate(script_files, start=1):
        script_name = script_file.replace('.py', '')
        scripts[str(index)] = {
            "name": script_name,
            "path": os.path.join(script_dir, script_file),
            "requirements": os.path.join(requirements_dir, f"{script_name}.txt")
        }
    return scripts

def main():
    script_dir = 'src'
    requirements_dir = 'requirements'

    scripts = discover_scripts(script_dir, requirements_dir)
    
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

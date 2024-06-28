"""
Version: 1.1.1
Author: Minemetero
"""
import os
import subprocess
import sys
import importlib

def check_package_installed(package):
    try:
        importlib.import_module(package)
        return True
    except ImportError:
        return False

def install_packages(packages):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
    except Exception as e:
        print(f"An error occurred while installing packages: {e}")

def get_package_import_name(package):
    package_import_name_mapping = {
        "numpy": "numpy",
        "sympy": "sympy",
        "matplotlib": "matplotlib",
        "turtle": "turtle"
        # Add other mappings if needed
    }
    return package_import_name_mapping.get(package, package)

def run_script(script_path, required_packages):
    packages_to_install = []

    for package in required_packages:
        package_import_name = get_package_import_name(package)
        if not check_package_installed(package_import_name):
            print(f"The package '{package}' is not installed.")
            install = input(f"Do you want to install '{package}'? (y/n): ").strip().lower()
            if install == 'y':
                packages_to_install.append(package)
            else:
                print(f"Skipping the installation of '{package}'.")

    if packages_to_install:
        install_packages(packages_to_install)
    
    try:
        # Execute the selected script
        os.system(f'python {script_path}')
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
    
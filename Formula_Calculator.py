"""
Version: 1.1
Author: Minemetero
"""

import math

print("Choose a kinematic equation to use:")
print("1: Vf = Vi + a * t")
print("2: Df = Di + Vi * t + 0.5 * a * t**2")
print("3: Vf_squared = Vi**2 + 2 * a * (Df - Di)")
print("4. avg_D = ((Vi + Vf) / 2) * t")
print("5. Vf = ((Vi**2 + 2 * a * (Df - Di))**0.5)")
print("6. Df = Vf * t - 0.5 * a * t**2")
print("7. Df = (Vf**2 - Vi**2) / (2 * a)")
print("8. a = (Vf - Vi) / t")
print("9. avg_D = 0.5 * a * t**2")

# User input to choose equation
equation_choice = input("Choose the equation number (1-9): ")

# Define the possible unknown variables for each equation
equation_variables = {
    '1': ['Vf', 'Vi', 'a', 't'],
    '2': ['Df', 'Di', 'Vi', 'a', 't'],
    '3': ['Vf_squared', 'Vi_squared', 'a', 'Df', 'Di'],
    '4': ['avg_D', 'Vi', 'Vf', 't'],
    '5': ['Vf', 'Vi_squared', 'a', 'Df', 'Di'],
    '6': ['Df', 'Vf', 'a', 't'],
    '7': ['Df', 'Vf_squared', 'Vi_squared', 'a'],
    '8': ['a', 'Vf', 'Vi', 't'],
    '9': ['avg_D', 'a', 't']
}

# Validate the equation choice
if equation_choice in equation_variables:
    # Ask for the unknown variable based on the chosen equation
    unknown_variable = input(f"Choose the unknown variable {equation_variables[equation_choice]}: ")
    
    # Ensure the unknown variable is valid for the chosen equation
    if unknown_variable in equation_variables[equation_choice]:
        # Handle each equation and calculate the unknown variable
        if equation_choice == '1':
            if unknown_variable == 'Vf':
                Vi = float(input("Enter initial velocity (Vi): "))
                a = float(input("Enter acceleration (a): "))
                t = float(input("Enter time (t): "))
                Vf = Vi + a * t
                print("Final velocity (Vf) =", Vf)
            elif unknown_variable == 'Vi':
                Vf = float(input("Enter final velocity (Vf): "))
                a = float(input("Enter acceleration (a): "))
                t = float(input("Enter time (t): "))
                Vi = Vf - a * t
                print("Initial velocity (Vi) =", Vi)
            elif unknown_variable == 'a':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                a = (Vf - Vi) / t
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                a = float(input("Enter acceleration (a): "))
                t = (Vf - Vi) / a
                print("Time (t) =", t)
        elif equation_choice == '2':
            if unknown_variable == 'Df':
                Di = float(input("Enter initial displacement (Di): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                a = float(input("Enter acceleration (a): "))
                t = float(input("Enter time (t): "))
                Df = Di + Vi * t + 0.5 * a * t**2
                print("Final displacement (Df) =", Df)
            elif unknown_variable == 'Di':
                Df = float(input("Enter final displacement (Df): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                a = float(input("Enter acceleration (a): "))
                t = float(input("Enter time (t): "))
                Di = Df - Vi * t - 0.5 * a * t**2
                print("Initial displacement (Di) =", Di)
            elif unknown_variable == 'a':
                Di = float(input("Enter initial displacement (Di): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                Df = float(input("Enter final displacement (Df): "))
                t = float(input("Enter time (t): "))
                a = (Df - Di - Vi * t) / (0.5 * t**2)
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                Di = float(input("Enter initial displacement (Di): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                Df = float(input("Enter final displacement (Df): "))
                a = float(input("Enter acceleration (a): "))
                t1 = (-Vi + math.sqrt(Vi**2 - 4 * 0.5 * a * (Di - Df))) / (2 * 0.5 * a)
                t2 = (-Vi - math.sqrt(Vi**2 - 4 * 0.5 * a * (Di - Df))) / (2 * 0.5 * a)
                t = t1 if t1 > 0 else t2
                print("Time (t) =", t)
        elif equation_choice == '3':
            if unknown_variable == 'Vf_squared':
                Vi = float(input("Enter initial velocity (Vi): "))
                a = float(input("Enter acceleration (a): "))
                Df = float(input("Enter final displacement (Df): "))
                Di = float(input("Enter initial displacement (Di): "))
                Vf_squared = Vi**2 + 2 * a * (Df - Di)
                print("Final velocity squared (Vf_squared) =", Vf_squared)
            elif unknown_variable == 'Vi_squared':
                Vf_squared = float(input("Enter final velocity squared (Vf_squared): "))
                a = float(input("Enter acceleration (a): "))
                Df = float(input("Enter final displacement (Df): "))
                Di = float(input("Enter initial displacement (Di): "))
                Vi_squared = Vf_squared - 2 * a * (Df - Di)
                Vi = math.sqrt(Vi_squared)
                print("Initial velocity squared (Vi_squared) =", Vi_squared)
                print("Initial velocity (Vi) =", Vi)
            elif unknown_variable == 'a':
                Vi_squared = float(input("Enter initial velocity squared (Vi_squared): "))
                Vf_squared = float(input("Enter final velocity squared (Vf_squared): "))
                Df = float(input("Enter final displacement (Df): "))
                Di = float(input("Enter initial displacement (Di): "))
                a = (Vf_squared - Vi_squared) / (2 * (Df - Di))
                print("Acceleration (a) =", a)
            elif unknown_variable == 'Df':
                Vi_squared = float(input("Enter initial velocity squared (Vi_squared): "))
                Vf_squared = float(input("Enter final velocity squared (Vf_squared): "))
                a = float(input("Enter acceleration (a): "))
                Df = ((Vf_squared - Vi_squared) / (2 * a))
                print("Final displacement (Df) =", Df)
        elif equation_choice == '4':
            if unknown_variable == 'avg_D':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                avg_D = ((Vi + Vf) / 2) * t
                print("Average displacement (avg_D) =", avg_D)
            elif unknown_variable == 'Vi':
                avg_D = float(input("Enter average displacement (avg_D): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                Vi = (2 * avg_D / t) - Vf
                print("Initial velocity (Vi) =", Vi)
            elif unknown_variable == 'Vf':
                avg_D = float(input("Enter average displacement (avg_D): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                t = float(input("Enter time (t): "))
                Vf = (2 * avg_D / t) - Vi
                print("Final velocity (Vf) =", Vf)
            elif unknown_variable == 't':
                avg_D = float(input("Enter average displacement (avg_D): "))
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = (2 * avg_D) / (Vi + Vf)
                print("Time (t) =", t)
        elif equation_choice == '5':
            if unknown_variable == 'Vf':
                Vi_squared = float(input("Enter initial velocity squared (Vi_squared): "))
                a = float(input("Enter acceleration (a): "))
                Di = float(input("Enter initial displacement (Di): "))
                Df = float(input("Enter final displacement (Df): "))
                Vf = math.sqrt(Vi_squared + 2 * a * (Df - Di))
                print("Final velocity (Vf) =", Vf)
            elif unknown_variable == 'a':
                Vi_squared = float(input("Enter initial velocity squared (Vi_squared): "))
                Vf_squared = float(input("Enter final velocity squared (Vf_squared): "))
                Df = float(input("Enter final displacement (Df): "))
                Di = float(input("Enter initial displacement (Di): "))
                a = (Vf_squared - Vi_squared) / (2 * (Df - Di))
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                a = float(input("Enter acceleration (a): "))
                t = (Vf - Vi) / a
                print("Time (t) =", t)
        elif equation_choice == '6':
            if unknown_variable == 'Df':
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                a = float(input("Enter acceleration (a): "))
                Df = Vf * t - 0.5 * a * t**2
                print("Final displacement (Df) =", Df)
            elif unknown_variable == 't':
                Vf = float(input("Enter final velocity (Vf): "))
                Di = float(input("Enter initial displacement (Di): "))
                a = float(input("Enter acceleration (a): "))
                t = (Vf - Di) / a
                print("Time (t) =", t)
            elif unknown_variable == 'a':
                Vf = float(input("Enter final velocity (Vf): "))
                Di = float(input("Enter initial displacement (Di): "))
                t = float(input("Enter time (t): "))
                a = (Vf - Di) / t
                print("Acceleration (a) =", a)
        elif equation_choice == '7':
            if unknown_variable == 'Df':
                Vf_squared = float(input("Enter final velocity squared (Vf_squared): "))
                Vi_squared = float(input("Enter initial velocity squared (Vi_squared): "))
                a = float(input("Enter acceleration (a): "))
                Df = (Vf_squared - Vi_squared) / (2 * a)
                print("Final displacement (Df) =", Df)
            elif unknown_variable == 'a':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                a = (Vf - Vi) / t
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                a = float(input("Enter acceleration (a): "))
                t = (Vf - Vi) / a
                print("Time (t) =", t)
        elif equation_choice == '8':
            if unknown_variable == 'a':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                a = (Vf - Vi) / t
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                Vi = float(input("Enter initial velocity (Vi): "))
                Vf = float(input("Enter final velocity (Vf): "))
                a = float(input("Enter acceleration (a): "))
                t = (Vf - Vi) / a
                print("Time (t) =", t)
            elif unknown_variable == 'Vf':
                Vi = float(input("Enter initial velocity (Vi): "))
                t = float(input("Enter time (t): "))
                a = float(input("Enter acceleration (a): "))
                Vf = Vi + a * t
                print("Final velocity (Vf) =", Vf)
            elif unknown_variable == 'Vi':
                Vf = float(input("Enter final velocity (Vf): "))
                t = float(input("Enter time (t): "))
                a = float(input("Enter acceleration (a): "))
                Vi = Vf - a * t
                print("Initial velocity (Vi) =", Vi)
        elif equation_choice == '9':
            if unknown_variable == 'avg_D':
                a = float(input("Enter acceleration (a): "))
                t = float(input("Enter time (t): "))
                avg_D = 0.5 * a * t**2
                print("Average displacement (avg_D) =", avg_D)
            elif unknown_variable == 'a':
                avg_D = float(input("Enter average distance (avg_D): "))
                t = float(input("Enter time (t): "))
                a = (2 * avg_D) / t**2
                print("Acceleration (a) =", a)
            elif unknown_variable == 't':
                avg_D = float(input("Enter average distance (avg_D): "))
                a = float(input("Enter acceleration (a): "))
                t = math.sqrt(2 * avg_D / a)
                print("Time (t) =", t)
    else:
        print("Invalid unknown variable. Please restart and choose a valid variable.")
else:
    print("Invalid equation choice. Please restart and choose a number between 1 and 9.")

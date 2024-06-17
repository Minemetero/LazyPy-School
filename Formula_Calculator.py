"""
Version: 1.2
Author: Minemetero
"""
import math

def input_float(prompt):
    return float(input(prompt))

def calculate_equation_1(unknown):
    if unknown == 'Vf':
        Vi = input_float("Enter initial velocity (Vi): ")
        a = input_float("Enter acceleration (a): ")
        t = input_float("Enter time (t): ")
        Vf = Vi + a * t
        return f"Final velocity (Vf) = {Vf}"
    elif unknown == 'Vi':
        Vf = input_float("Enter final velocity (Vf): ")
        a = input_float("Enter acceleration (a): ")
        t = input_float("Enter time (t): ")
        Vi = Vf - a * t
        return f"Initial velocity (Vi) = {Vi}"
    elif unknown == 'a':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        a = (Vf - Vi) / t
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        a = input_float("Enter acceleration (a): ")
        t = (Vf - Vi) / a
        return f"Time (t) = {t}"

def calculate_equation_2(unknown):
    if unknown == 'Df':
        Di = input_float("Enter initial displacement (Di): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        a = input_float("Enter acceleration (a): ")
        t = input_float("Enter time (t): ")
        Df = Di + Vi * t + 0.5 * a * t**2
        return f"Final displacement (Df) = {Df}"
    elif unknown == 'Di':
        Df = input_float("Enter final displacement (Df): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        a = input_float("Enter acceleration (a): ")
        t = input_float("Enter time (t): ")
        Di = Df - Vi * t - 0.5 * a * t**2
        return f"Initial displacement (Di) = {Di}"
    elif unknown == 'a':
        Di = input_float("Enter initial displacement (Di): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        Df = input_float("Enter final displacement (Df): ")
        t = input_float("Enter time (t): ")
        a = (Df - Di - Vi * t) / (0.5 * t**2)
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        Di = input_float("Enter initial displacement (Di): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        Df = input_float("Enter final displacement (Df): ")
        a = input_float("Enter acceleration (a): ")
        discriminant = Vi**2 + 2 * a * (Df - Di)
        if discriminant < 0:
            return "No real solution for time."
        t1 = (-Vi + math.sqrt(discriminant)) / a
        t2 = (-Vi - math.sqrt(discriminant)) / a
        t = max(t1, t2)
        return f"Time (t) = {t}"

def calculate_equation_3(unknown):
    if unknown == 'Vf_squared':
        Vi = input_float("Enter initial velocity (Vi): ")
        a = input_float("Enter acceleration (a): ")
        Df = input_float("Enter final displacement (Df): ")
        Di = input_float("Enter initial displacement (Di): ")
        Vf_squared = Vi**2 + 2 * a * (Df - Di)
        return f"Final velocity squared (Vf_squared) = {Vf_squared}"
    elif unknown == 'Vi_squared':
        Vf_squared = input_float("Enter final velocity squared (Vf_squared): ")
        a = input_float("Enter acceleration (a): ")
        Df = input_float("Enter final displacement (Df): ")
        Di = input_float("Enter initial displacement (Di): ")
        Vi_squared = Vf_squared - 2 * a * (Df - Di)
        return f"Initial velocity squared (Vi_squared) = {Vi_squared}"
    elif unknown == 'a':
        Vi_squared = input_float("Enter initial velocity squared (Vi_squared): ")
        Vf_squared = input_float("Enter final velocity squared (Vf_squared): ")
        Df = input_float("Enter final displacement (Df): ")
        Di = input_float("Enter initial displacement (Di): ")
        a = (Vf_squared - Vi_squared) / (2 * (Df - Di))
        return f"Acceleration (a) = {a}"
    elif unknown == 'Df':
        Vi_squared = input_float("Enter initial velocity squared (Vi_squared): ")
        Vf_squared = input_float("Enter final velocity squared (Vf_squared): ")
        a = input_float("Enter acceleration (a): ")
        Df = (Vf_squared - Vi_squared) / (2 * a)
        return f"Final displacement (Df) = {Df}"

def calculate_equation_4(unknown):
    if unknown == 'avg_D':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        avg_D = ((Vi + Vf) / 2) * t
        return f"Average displacement (avg_D) = {avg_D}"
    elif unknown == 'Vi':
        avg_D = input_float("Enter average displacement (avg_D): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        Vi = (2 * avg_D / t) - Vf
        return f"Initial velocity (Vi) = {Vi}"
    elif unknown == 'Vf':
        avg_D = input_float("Enter average displacement (avg_D): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        t = input_float("Enter time (t): ")
        Vf = (2 * avg_D / t) - Vi
        return f"Final velocity (Vf) = {Vf}"
    elif unknown == 't':
        avg_D = input_float("Enter average displacement (avg_D): ")
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = (2 * avg_D) / (Vi + Vf)
        return f"Time (t) = {t}"

def calculate_equation_5(unknown):
    if unknown == 'Vf':
        Vi_squared = input_float("Enter initial velocity squared (Vi_squared): ")
        a = input_float("Enter acceleration (a): ")
        Df = input_float("Enter final displacement (Df): ")
        Di = input_float("Enter initial displacement (Di): ")
        Vf = math.sqrt(Vi_squared + 2 * a * (Df - Di))
        return f"Final velocity (Vf) = {Vf}"
    elif unknown == 'a':
        Vi_squared = input_float("Enter initial velocity squared (Vi_squared): ")
        Vf_squared = input_float("Enter final velocity squared (Vf_squared): ")
        Df = input_float("Enter final displacement (Df): ")
        Di = input_float("Enter initial displacement (Di): ")
        a = (Vf_squared - Vi_squared) / (2 * (Df - Di))
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        a = input_float("Enter acceleration (a): ")
        t = (Vf - Vi) / a
        return f"Time (t) = {t}"

def calculate_equation_6(unknown):
    if unknown == 'Df':
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        a = input_float("Enter acceleration (a): ")
        Df = Vf * t - 0.5 * a * t**2
        return f"Final displacement (Df) = {Df}"
    elif unknown == 't':
        Vf = input_float("Enter final velocity (Vf): ")
        Di = input_float("Enter initial displacement (Di): ")
        a = input_float("Enter acceleration (a): ")
        t = (Vf - Di) / a
        return f"Time (t) = {t}"
    elif unknown == 'a':
        Vf = input_float("Enter final velocity (Vf): ")
        Di = input_float("Enter initial displacement (Di): ")
        t = input_float("Enter time (t): ")
        a = (Vf - Di) / t
        return f"Acceleration (a) = {a}"

def calculate_equation_7(unknown):
    if unknown == 'Df':
        Vf_squared = input_float("Enter final velocity squared (Vf_squared): ")
        Vi_squared = input_float("Enter initial velocity squared (Vi_squared): ")
        a = input_float("Enter acceleration (a): ")
        Df = (Vf_squared - Vi_squared) / (2 * a)
        return f"Final displacement (Df) = {Df}"
    elif unknown == 'a':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        a = (Vf - Vi) / t
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        a = input_float("Enter acceleration (a): ")
        t = (Vf - Vi) / a
        return f"Time (t) = {t}"

def calculate_equation_8(unknown):
    if unknown == 'a':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        a = (Vf - Vi) / t
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        Vi = input_float("Enter initial velocity (Vi): ")
        Vf = input_float("Enter final velocity (Vf): ")
        a = input_float("Enter acceleration (a): ")
        t = (Vf - Vi) / a
        return f"Time (t) = {t}"
    elif unknown == 'Vf':
        Vi = input_float("Enter initial velocity (Vi): ")
        t = input_float("Enter time (t): ")
        a = input_float("Enter acceleration (a): ")
        Vf = Vi + a * t
        return f"Final velocity (Vf) = {Vf}"
    elif unknown == 'Vi':
        Vf = input_float("Enter final velocity (Vf): ")
        t = input_float("Enter time (t): ")
        a = input_float("Enter acceleration (a): ")
        Vi = Vf - a * t
        return f"Initial velocity (Vi) = {Vi}"

def calculate_equation_9(unknown):
    if unknown == 'avg_D':
        a = input_float("Enter acceleration (a): ")
        t = input_float("Enter time (t): ")
        avg_D = 0.5 * a * t**2
        return f"Average displacement (avg_D) = {avg_D}"
    elif unknown == 'a':
        avg_D = input_float("Enter average displacement (avg_D): ")
        t = input_float("Enter time (t): ")
        a = (2 * avg_D) / t**2
        return f"Acceleration (a) = {a}"
    elif unknown == 't':
        avg_D = input_float("Enter average displacement (avg_D): ")
        a = input_float("Enter acceleration (a): ")
        t = math.sqrt(2 * avg_D / a)
        return f"Time (t) = {t}"

equation_handlers = {
    '1': calculate_equation_1,
    '2': calculate_equation_2,
    '3': calculate_equation_3,
    '4': calculate_equation_4,
    '5': calculate_equation_5,
    '6': calculate_equation_6,
    '7': calculate_equation_7,
    '8': calculate_equation_8,
    '9': calculate_equation_9
}

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
        # Calculate the unknown variable
        result = equation_handlers[equation_choice](unknown_variable)
        print(result)
    else:
        print("Invalid unknown variable. Please restart and choose a valid variable.")
else:
    print("Invalid equation choice. Please restart and choose a number between 1 and 9.")

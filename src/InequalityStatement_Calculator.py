"""
Version: 1.0.0
Author: Minemetero
"""
import sympy

def solve_inequality(inequality_str):
    # Define the variable
    x = sympy.symbols('x')
    
    # Parse the inequality string into a sympy expression
    inequality = sympy.sympify(inequality_str)
    
    # Solve the inequality
    solution = sympy.solve(inequality, x)
    
    return solution

# Get the inequality statement from the user
inequality_str = input("Enter an inequality (e.g., '2*x + 3 < 7'): ")

# Solve the inequality
solution = solve_inequality(inequality_str)

# Print the solution
print("Solution:", solution)

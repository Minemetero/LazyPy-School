"""
Version: 1.0.0
Author: Minemetero
"""
from sympy import symbols, solve, sympify

def solve_inequality(inequality_str):
    # Define the variable
    x = symbols('x')
    
    # Parse the inequality string into a sympy expression
    inequality = sympify(inequality_str)
    
    # Solve the inequality
    solution = solve(inequality, x)
    
    return solution

# Get the inequality statement from the user
inequality_str = input("Enter an inequality (e.g., '2*x + 3 < 7'): ")

# Solve the inequality
solution = solve_inequality(inequality_str)

# Print the solution
print("Solution:", solution)

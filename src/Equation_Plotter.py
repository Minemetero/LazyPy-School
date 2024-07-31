"""
Version: 0.1.0
Author: Minemetero
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_equation(equation, x_range, y_range, title="Equation Plot"):
    """
    Plots a given mathematical equation.

    Parameters:
    equation (str): The equation to plot, with 'x' as the variable.
    x_range (tuple): The range of x values (min, max).
    y_range (tuple): The range of y values (min, max).
    title (str): The title of the plot.
    """
    # Define the x values
    x = np.linspace(x_range[0], x_range[1], 400)
    
    try:
        # Define the y values by evaluating the equation
        y = eval(equation)
    except Exception as e:
        print(f"Error in equation: {e}")
        return
    
    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {equation}')
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def get_range(prompt):
    """
    Prompts the user for a range and returns it as a tuple.
    """
    while True:
        try:
            range_input = input(prompt)
            range_values = tuple(map(float, range_input.split(',')))
            if len(range_values) == 2 and range_values[0] < range_values[1]:
                return range_values
            else:
                print("Please enter two numbers separated by a comma, where the first number is less than the second.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")

def main():
    print("Welcome to the Equation Plotter!")
    
    # Input equation from user
    while True:
        user_equation = input("Enter the equation in terms of 'x' (e.g., x**2 + 2*x + 1): ")
        try:
            # Test if the equation can be evaluated
            x = np.linspace(-10, 10, 10)
            y = eval(user_equation)
            if isinstance(y, np.ndarray):
                break
        except Exception as e:
            print(f"Invalid equation: {e}")
    
    # Get x range from user
    x_range = get_range("Enter the x range as two numbers separated by a comma (e.g., -10, 10): ")

    # Get y range from user
    y_range = get_range("Enter the y range as two numbers separated by a comma (e.g., -10, 10): ")

    # Plot the equation
    plot_equation(user_equation, x_range, y_range)

if __name__ == "__main__":
    main()

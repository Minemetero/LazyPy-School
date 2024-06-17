"""
Version: 1.0
Author: Minemetero
"""

import matplotlib.pyplot as plt
import numpy as np

def draw_number_line(input_str):
    try:
        # Split the input string by commas to support multiple numbers or formulas
        numbers = [eval(num.strip()) for num in input_str.split(',')]
    except Exception as e:
        print(f"Error evaluating input: {e}")
        return
    
    # Define the range of the number line
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Create the number line
    fig, ax = plt.subplots(figsize=(15, 2))
    ax.plot(range(min_value, max_value + 1), [0] * (max_value - min_value + 1), marker='|', color='black')
    
    # Plot all numbers on the number line
    for i in range(min_value, max_value + 1):
        if i not in numbers:
            ax.text(i, 0.1, str(i), horizontalalignment='center')
    
    # Highlight the input numbers
    for number in numbers:
        ax.plot(number, 0, marker='o', color='red', markersize=10)
        ax.text(number, 0.2, str(number), horizontalalignment='center', color='red')
    
    # Set limits and remove y-axis
    ax.set_xlim(min_value - 1, max_value + 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    plt.title(f"Number Line for {', '.join(map(str, numbers))}")
    plt.show()

# Input multiple numbers or formulas
input_str = input("Enter numbers or formulas separated by commas: ")
draw_number_line(input_str)

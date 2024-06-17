"""
Version: 0.0.1
Author: Minemetero
"""
import turtle
import math

def draw_triangle(a, b, c):
    # Calculate the angles using the Law of Cosines
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B

    # Set up the screen
    screen = turtle.Screen()
    screen.title("Triangle Drawing")
    screen.bgcolor("white")

    # Create a turtle named "tri"
    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("black")

    # Set the speed of the turtle
    tri.speed(2)

    # Draw the triangle
    tri.forward(a)
    tri.left(180 - angle_B)
    tri.forward(b)
    tri.left(180 - angle_C)
    tri.forward(c)

    # Hide the turtle and display the window
    tri.hideturtle()
    screen.mainloop()

def get_side_length(prompt):
    while True:
        try:
            side_length = float(input(prompt))
            if side_length <= 0:
                print("Please enter a positive number.")
            else:
                return side_length
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Enter the lengths of the sides of the triangle:")
    a = get_side_length("Side a: ")
    b = get_side_length("Side b: ")
    c = get_side_length("Side c: ")

    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        draw_triangle(a, b, c)
    else:
        print("The entered sides do not form a valid triangle.")

# Run the main function
if __name__ == "__main__":
    main()

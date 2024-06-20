"""
Version: 1.0.0
Author: Minemetero
"""
import turtle
import math

def draw_triangle(a, b, c):
    # Calculate the angles using the Law of Cosines
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B

    # Calculate the vertices of the triangle
    A = (0, 0)
    B = (a, 0)
    C_x = b * math.cos(math.radians(angle_A))
    C_y = b * math.sin(math.radians(angle_A))
    C = (C_x, C_y)

    # Set up the screen
    screen = turtle.Screen()
    screen.title("Triangle Drawing")
    screen.bgcolor("white")

    # Create a turtle named "tri"
    tri = turtle.Turtle()
    tri.shape("turtle")
    tri.color("black")
    tri.speed(2)

    # Draw the triangle
    tri.penup()
    tri.goto(A)
    tri.pendown()
    tri.goto(B)
    tri.goto(C)
    tri.goto(A)

    # Label the angles
    tri.penup()
    tri.goto(A[0] - 20, A[1] - 20)
    tri.pendown()
    tri.write(f"{round(angle_A, 2)}°", align="center", font=("Arial", 12, "normal"))

    tri.penup()
    tri.goto(B[0] + 20, B[1] - 20)
    tri.pendown()
    tri.write(f"{round(angle_B, 2)}°", align="center", font=("Arial", 12, "normal"))

    tri.penup()
    tri.goto(C[0] + 20, C[1] + 20)
    tri.pendown()
    tri.write(f"{round(angle_C, 2)}°", align="center", font=("Arial", 12, "normal"))

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

def scale_sides(a, b, c, max_length=300):
    # Find the maximum side length
    max_side = max(a, b, c)
    # Scale down if any side is greater than the max_length
    if max_side > max_length:
        scale_factor = max_length / max_side
        a *= scale_factor
        b *= scale_factor
        c *= scale_factor
    # Ensure a minimum size to avoid very small triangles
    min_length = 50
    if max(a, b, c) < min_length:
        scale_factor = min_length / max(a, b, c)
        a *= scale_factor
        b *= scale_factor
        c *= scale_factor
    return a, b, c

def main():
    print("Enter the lengths of the sides of the triangle:")
    a = get_side_length("Side a: ")
    b = get_side_length("Side b: ")
    c = get_side_length("Side c: ")

    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Scale the sides to fit the screen
        a, b, c = scale_sides(a, b, c)
        draw_triangle(a, b, c)
    else:
        print("The entered sides do not form a valid triangle.")

# Run the main function
if __name__ == "__main__":
    main()

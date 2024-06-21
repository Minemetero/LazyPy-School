"""
Version: 0.0.3
Author: Minemetero
"""
import turtle
import math

def draw_triangle_sides(a, b, c):
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

def draw_triangle_angles(a, angle_B, angle_C):
    # Calculate the third angle
    angle_A = 180 - angle_B - angle_C

    # Calculate the other two sides using the Law of Sines
    b = a * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))
    c = a * math.sin(math.radians(angle_C)) / math.sin(math.radians(angle_A))

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

def get_angle(prompt):
    while True:
        try:
            angle = float(input(prompt))
            if angle <= 0 or angle >= 180:
                print("Please enter an angle between 0 and 180 degrees.")
            else:
                return angle
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
    print("Choose the method to define the triangle:")
    print("1. Input three sides")
    print("2. Input two angles and one side")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Enter the lengths of the sides of the triangle:")
        a = get_side_length("Side a: ")
        b = get_side_length("Side b: ")
        c = get_side_length("Side c: ")

        # Check if the sides form a valid triangle
        if a + b > c and a + c > b and b + c > a:
            # Scale the sides to fit the screen
            a, b, c = scale_sides(a, b, c)
            draw_triangle_sides(a, b, c)
        else:
            print("The entered sides do not form a valid triangle.")
    elif choice == "2":
        print("Enter one side and the two angles of the triangle:")
        a = get_side_length("Side a: ")
        angle_B = get_angle("Angle opposite to side b (in degrees): ")
        angle_C = get_angle("Angle opposite to side c (in degrees): ")

        # Calculate the third angle and the other two sides
        angle_A = 180 - angle_B - angle_C
        b = a * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))
        c = a * math.sin(math.radians(angle_C)) / math.sin(math.radians(angle_A))

        if a + b > c and a + c > b and b + c > a:
            # Scale the sides to fit the screen
            a, b, c = scale_sides(a, b, c)
            draw_triangle_angles(a, angle_B, angle_C)
        else:
            print("The entered side and angles do not form a valid triangle.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the main function
if __name__ == "__main__":
    main()

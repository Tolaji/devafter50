import math


class area:
    def compute_area_of_square():
        square_side_length = float(
            input("What is the length of a side of the square? ")
        )
        area_square = square_side_length * square_side_length
        return area_square

    def compute_area_of_rectangle():
        length_rectangle = float(input("What is the length of rectangle? "))
        width_rectangle = float(input("What is the width of rectangle? "))
        area_rectangle = length_rectangle * width_rectangle
        return area_rectangle

    def compute_area_of_circle():
        radius_circle = float(input("What is the radius of the circle? "))
        pi = 3.14
        area_circle = pi * (radius_circle**2)
        return area_circle


print("The area of the rectangle is: ", area_rectangle)
print("The area of the circle is: ", area_circle)

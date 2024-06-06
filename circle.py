#Write a Python class named Circle constructed by a radius and two
#methods which will compute the area and the perimeter of a circle


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    circle = Circle(5)

    print(f"The area of the circle is: {circle.area()}") 
    print(f"The perimeter of the circle is: {circle.perimeter()}")  

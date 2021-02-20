
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of this circle : {round(math.pi * (self.radius**2), 2)}")

    def perimeter(self):
        print(f"Perimeter of this circle : {round(2 * self.radius * math.pi, 2)}")


if __name__ == '__main__':

    p1 = Circle(10)
    p1.area()
    p1.perimeter()

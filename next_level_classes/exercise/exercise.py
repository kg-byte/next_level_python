# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Properties for classes
# Enhance the provided Python code by adding essential properties to the Circle class to ensure
# accurate functionality. Make sure to include suitable type annotations for clarity and correctness.
# The test code is designed to showcase the proper implementation of properties such as radius,
# diameter, area, and circumference within the Circle class. The tests are there too help you to see if
# the implementation is correct.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from dataclasses import dataclass
from math import pi

@dataclass
class Circle:
    _radius: float

    @property
    def radius(self) -> float:
        return self._radius
    # TODO: Add the properties

    @radius.setter
    def radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Circle radius can not be a negative value')
        self._radius = radius

    @property
    def diameter(self) -> float:
        return self._radius * 2
    
    @property
    def area(self) -> float:
        return pi* self._radius ** 2
    
    @property
    def circumference(self) -> float:
        return pi * self.diameter
    
def create_circle(radius: float) -> Circle:
    return Circle(radius)


def main() -> None:
    circle = create_circle(5.0)

    # Test the properties
    circle.radius = 10
    print("Radius:", circle.radius)
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)
    print("Circumference:", circle.circumference)


if __name__ == "__main__":
    main()

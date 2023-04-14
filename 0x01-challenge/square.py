#!/usr/bin/python3
"""
square class module
"""


class square():
    """Describes the square"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initializing the square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """create an object instance of a square class"""

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

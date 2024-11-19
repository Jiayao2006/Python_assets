from Shape import *


class Square(Shape):
    def __init__(self, side, length):
        super().__init__(side)
        self.length = length

    def calculate_perimeter(self):
        return self.length * 4

    def __str__(self):
        return f"Square with {self.side} and length of {self.length} has a perimeter of {self.calculate_perimeter()}"
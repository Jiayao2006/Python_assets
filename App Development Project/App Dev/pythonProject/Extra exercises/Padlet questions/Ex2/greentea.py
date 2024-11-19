from tea import *

class Greentea(Tea):
    def __init__(self, colour, taste):
        super().__init__("Sencha", "Japan", colour)
        self.taste = taste

    def total_caffeine(self, serving, weight):
        return serving * weight

    def __str__(self):
        return f"{super().__str__()} and {self.taste} taste"
from tea import Tea

class Blacktea(Tea):
    def __init__(self, name, origin, colour, aroma):
        Tea.__init__(self, name, origin, colour)
        self.aroma = aroma

    def __str__(self):
        return f"{super().__str__()} and {self.aroma} aroma"
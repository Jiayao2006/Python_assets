class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.__name}"


class BasketBallPlayer(Player):
    # Class attribute which is a list and the value is Guard, Center, Forward
    positions = ["Guard", "Center", "Forward"]

    def __init__(self, name):
        Player.__init__(self, name)
        self.__position = ""

    def get_position(self):
        return self.__position

    def set_position(self, position):
        # Yes, a valid position
        if position in self.__class__.positions:
            self.__position = position
        else:
            print("Invalid position for basketball player")

    def __str__(self):
        return f"{super().__str__()} playing as a {self.__position}"

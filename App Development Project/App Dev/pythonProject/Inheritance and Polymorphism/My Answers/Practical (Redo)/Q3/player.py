class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class BasketballPlayer(Player):
    positions = ["Guard", "Forward", "Center"]
    def __init__(self, name):
        super().__init__(name)
        self.__position = ""

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if position not in BasketballPlayer.positions:
            print("Invalid position for basketball player")
        else:
            self.__position = position

    def __str__(self):
        return f"Basketball Player: {self.get_name()}, Position: {self.get_position()}"

def main():
    members = []
    positions = []
    team = input("Enter basketball team name: ")
    for i in range(5):
        members.append(input("Enter the player name: "))
        positions.append(input("Which position is he/she playing? "))


    for i in members:
        player = Player(i)

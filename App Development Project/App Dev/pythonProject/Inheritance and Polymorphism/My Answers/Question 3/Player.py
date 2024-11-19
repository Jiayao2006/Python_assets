class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class BasketballPlayer(Player):
    positions = ["Guard", "Forward", "Center"]

    def __init__(self, name, position):
        super().__init__(name)
        self.set_position(position)

    def get_position(self):
        return self.__position

    def set_position(self, position):
        if position in BasketballPlayer.positions:
            self.__position = position
        else:
            raise ValueError("Invalid position for basketball player")

    def __str__(self):
        return f"Player: {self.get_name()}, Position: {self.get_position()}"


def main():
    team = []
    players_data = [
        ("Jordan", "Guard"),
        ("James", "Forward"),
        ("O'Neal", "Center"),
        ("Kobe", "Guard"),
        ("Tim Duncan", "Forward")
    ]

    for name, position in players_data:
        player = BasketballPlayer(name, position)
        team.append(player)

    print("Basketball Team:")
    for player in team:
        print(player)

if __name__ == "__main__":
    main()

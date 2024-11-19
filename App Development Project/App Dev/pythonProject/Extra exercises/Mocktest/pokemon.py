class Pokemon:
    balance = 50

    def __init__(self, name, defence):
        self.__name = name
        self.__attack = 0
        self.__defence = defence
        Pokemon.balance -= 1

    def get_name(self):
        return self.__name

    def get_attack(self):
        return self.__attack

    def get_defence(self):
        return self.__defence

    def set_name(self, name):
        self.__name = name

    def set_defence(self, defence):
        self.__defence = defence

    def set_attack(self, attack):
        if attack >= self.get_defence():
            self.__attack = attack


def main():
    for i in range(2):
        name = input("Enter Pokemon name: ")
        attack = int(input("Enter Pokemon attack: "))
        defence = int(input("Enter Pokemon defence: "))

        pokemon = Pokemon(name, defence)
        pokemon.set_attack(attack)

        print(f"Pokemon {pokemon.get_name()} with attack {pokemon.get_attack()} and defense {pokemon.get_defence()}")

    print(Pokemon.balance, "Pokemon(s) remaining")

if __name__ == '__main__':
    main()

from Monster import Monster
from Monster import WaterMonster
from Monster import GrassMonster
from Monster import FireMonster


def main():
    monster = Monster("Giant", 17, 6, 7)
    firemonster = FireMonster()
    watermonster = WaterMonster()
    grassmonster = GrassMonster()
    print(monster.display())
    print(firemonster.display())
    print(watermonster.display())
    print(grassmonster.display())

if __name__ == "__main__":
    main()
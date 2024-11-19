from Monster import Monster
from Monster import WaterMonster
from Monster import GrassMonster
from Monster import FireMonster

def display_info(monster):
    if isinstance(monster, Monster):
        monster.display()
    else:
        print("Invalid Monster")

def main():
    monster = Monster("Giant", 17, 6, 7)
    firemonster = FireMonster()
    watermonster = WaterMonster()
    grassmonster = GrassMonster()
    display_info(monster)
    display_info(firemonster)
    display_info(watermonster)
    display_info(grassmonster)
    display_info("not_a_monster")


if __name__ == "__main__":
    main()
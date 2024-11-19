from tea import *
from Blacktea import *
from greentea import *


def main():
    blacketea = Blacktea("Darjeeling", "India", "golden-yellow", "floral")
    greentea = Greentea("bright-green", "grassy")
    check_tea(blacketea)
    check_tea(greentea)

def check_tea(tea):
    if isinstance(tea, Blacktea):
        print(tea)
        print(f"Each brewed pot of tea is sold for ${tea.compute_price(4, 5.15):.2f}")

    if isinstance(tea, Greentea):
        print(tea)
        print(f"Each brewed pot  of tea contains {tea.total_caffeine(5, 0.7)}g of caffeine")

if __name__ == '__main__':
    main()
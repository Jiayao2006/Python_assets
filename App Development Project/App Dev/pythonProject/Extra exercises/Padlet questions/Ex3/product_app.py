def load_data():
    # continue your code here
    with open("data.txt", "r") as file:
        for lines in file:
            print(lines.strip())

def potential_earnings():
    earnings = 0
    with open("data.txt", "r") as file:
        for lines in file:
            data = lines.strip().split(",")
            price = float(data[1])
            qty = int(data[2])
            earnings += (price*qty)

    return f"Potential earnings from selling the products are ${earnings:.2f}"

while True:
    print("Enter 1 for Displaying Data")
    print("Enter 2 for Calculating Potential Earnings")
    print("Enter any other numbers to end the program")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        choice = 0
    if choice == 1:
        load_data()
    elif choice == 2:
        print(potential_earnings())
    else:
        break

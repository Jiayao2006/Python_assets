try:
    count = int(input("How many number you want to replace? "))
    if count <= 0:
        raise ValueError("Count must be positive")
    numList = []
    for i in range(count):
        try:
            num = int(input(f"Enter number {i+1}: "))
            numList.append(num)
        except ValueError:
            print("Please try a valid number. Try again.")

    print(f"The lowest number in the list: {min(numList)}")
    print(f"The highest number in the list: {max(numList)}")
    print(f"The total number in the list: {sum(numList)}")
    print(f"The average of the number in the list: {sum(numList) / len(numList)}")

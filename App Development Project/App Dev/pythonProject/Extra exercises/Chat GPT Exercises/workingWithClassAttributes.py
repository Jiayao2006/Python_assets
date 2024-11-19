class Dog:
    def __init__(self, breed):
        self.__breed = breed

    def bark(self):
        print(self.__breed, "Woof!")


dog1 = Dog("Golden Retriever")
dog2 = Dog("Shiba Inu")

dog1.bark()
dog2.bark()
class Course:
    count = 0

    def __init__(self, name, intake):
        self.__name = name
        self.__intake = intake
        self.__class__.count += 1

    def get_name(self):
        return self.__name

    def get_intake(self):
        return self.__intake

    def set_name(self, name):
        self.__name = name

    def set_intake(self, intake):
        self.__intake = intake

    def get_course_info(self):
        print(f"Name: {self.get_name()}, intake: {self.get_intake()}\n"
              f"{self.__class__.count} Course(s) created")

def main():
    diploma = Course("Diploma in IT", 80)
    try:
        new_intake = int(input("Enter new intake: "))
        diploma.set_intake(new_intake)
        diploma.get_course_info()
    except ValueError:
        print("Enter an integer/whole number")

if __name__ == '__main__':
    main()



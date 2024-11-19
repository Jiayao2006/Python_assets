class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = []

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4


def main():
    students = load_result()
    for s in students:
        print(f"{s.name} {s.get_score()}")


def load_result():
    students = []
    # implement the load result logic here
    return students


# start the test program
main()  

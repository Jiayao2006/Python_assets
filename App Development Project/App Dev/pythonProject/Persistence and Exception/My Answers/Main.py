class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = ["School A", "School B", "School C"]

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4


def main():
    students = load_result()
    for s in students:
        print(f"{s.name} {s.get_score()}, the choices are {", ".join(s.choices)}")


def load_result():
    students = []
    try:
        with open("Question 3/results.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                names = data[0]
                scores = list(map(int, data[1:]))
                student = Student(names)
                student.math, student.chinese, student.english, student.science = scores
                students.append(student)
    except FileNotFoundError:
        print("File not found")

    return students


# start the test program
main()  

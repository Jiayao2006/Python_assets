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
    try:
        for s in students:
            s.choices.append("School A")
            s.choices.append("School B")
            s.choices.append("School C")
            print(f"{s.name} {s.get_score()}, the choices are {s.choices[0]}, {s.choices[1]}, {s.choices[2]}")
    except:
        print("Unknown Error")


def load_result(): # returns a list
    students = []
    # implement the load result logic here
    try:
        with open("results.txt", "r") as file1:
            for lines in file1:
                data = lines.strip().split(",") # returns a list of split up strings
                name = data[0]
                student = Student(name)
                student.math, student.chinese, student.english, student.science = list(map(int, data[1:])) # convert the number strings into integer and assigns it to the subjects respectively
                students.append(student)
        return students
    except FileNotFoundError:
        print("File not found")




# start the test program
main()  

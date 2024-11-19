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
        s.choices.append("SchoolA")
        s.choices.append("SchoolB")
        s.choices.append("SchoolC")
        print(f"{s.name} scores {s.get_score():.2f}, "
              f"the choices are {s.choices[0]}, {s.choices[1]}, {s.choices[2]}")


def load_result():
    students = []
    try:
        result_file = open("results.txt", "r")
        for result in result_file: 
            list = result.split(",")
            s = Student(list[0])
            s.math = float(list[1])
            s.chinese = float(list[2])  
            s.english = float(list[3])  
            s.science = float(list[4]) 
            students.append(s)  
    except IOError:  
        print("File not found")
    finally:
        result_file.close()
  
    return students


# start the test program
main()  

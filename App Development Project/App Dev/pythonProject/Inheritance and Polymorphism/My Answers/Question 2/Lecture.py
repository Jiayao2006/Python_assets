from question1 import Person
from Student import Student

class Lecture(Person):
    def __init__(self, nric, name, staff_id, teaching_hours):
        super().__init__(nric, name)
        self.__staff_id = staff_id
        self.__teaching_hours = teaching_hours

    def get_staff_id(self):
        return self.__staff_id

    def get_teaching_hours(self):
        return self.__teaching_hours

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_teaching_hours(self, hours):
        self.__teaching_hours = hours

    def compute_salary(self):
        return self.__teaching_hours * 90

    def __str__(self):
        return (f"Name: {self.get_name()}\nNRIC: {self.get_nric()}\nStaff: {self.get_staff_id()}\n"
                f"Teaching Hours: {self.get_teaching_hours()}\nSalary: {self.compute_salary()}")


def main():
    print("Enter Lecturer's details:")
    name = input("Enter name: ")
    nric = input("Enter NRIC: ")
    while True:
        staff = input("Enter staff ID: ")
        if staff == nric:
            break
        else:
            print("Staff ID needs to be the same as NRIC")
    teaching_hours = int(input("Enter teaching hours: "))

    lecture = Lecture(nric, name, staff, teaching_hours)

    print("\nLecture Details:")
    print(lecture)

    print("Enter student details: ")
    nric = input("Enter NRIC: ")
    name = input("Enter name: ")
    test_mark = float(input("Enter test marks: "))
    exam_mark = float(input("Enter exam marks: "))

    student = Student(nric, name, test_mark, exam_mark)
    print("Student's Details: ")
    print(student)


if __name__ == "__main__":
    main()

from Lecturer import Lecturer
from person import Person
from student import Student

def nric_and_staffID_checker(nric, staffID):
    match = True
    if nric == staffID:
        return match
    else:
        match = False
        return match


def main():
    name = input("Enter Lecturer Name: ")
    nric = input("Enter NRIC: ")
    while True:
        staffID = input("Enter staff ID: ")
        if nric_and_staffID_checker(nric, staffID) == False:
            print("Staff ID needs to be the same as NRIC")
        else:
            break
    teachingHours = float(input("Enter total teaching hour: "))

    lecturer = Lecturer(name, nric, staffID)
    lecturer.set_total_teaching_hour(teachingHours)

    name = input("Enter Student Name: ")
    nric = input("Enter Student NRIC: ")
    admin_no = input("Enter admin number: ")
    while True:
        test_mark = float(input("Enter test mark: "))
        if 0<=test_mark<=100:
            break
        else:
            print("Test marks must be between 0 to 100 (inclusive)")

    while True:
        exam_mark = float(input("Enter exam mark: "))
        if 0<=exam_mark<=100:
            break
        else:
            print("Exam marks must be between 0 to 100 (inclusive)")
    student = Student(name, nric, admin_no)
    student.set_exam_mark(exam_mark)
    student.set_test_mark(test_mark)
    print(lecturer)
    print(student)

main()
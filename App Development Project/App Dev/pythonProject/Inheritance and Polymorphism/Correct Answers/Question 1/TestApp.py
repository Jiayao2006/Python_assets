from Lecturer import *
from Student import *

name = input("Enter Lecturer Name: ")
nric = input("Enter Lecturer NRIC: ")
staff_id = input("Enter Staff Id: ")
hour = float(input("Enter Total Teaching Hour: "))
lecturer_1 = Lecturer(name, nric, staff_id)
lecturer_1.set_total_teaching_hour(hour)

name = input("Enter Student Name: ")
nric = input("Enter Student NRIC: ")
admin_no = input("Enter Student Admin No: ")
test_mark = float(input("Enter Test mark: "))
exam_mark = float(input("Enter Exam mark: "))

student_1 = Student(name, nric, admin_no)
student_1.set_test_mark(test_mark)
student_1.set_exam_mark(exam_mark)

print(lecturer_1)
print(student_1)

from Lecturer import *
from Student import *

name = input("Enter Lecturer Name: ")
nric = input("Enter Lecturer NRIC: ")

while True:
    staff_id = input("Enter Staff Id: ")
    if staff_id == nric:
        break
    else:
        print("Staff Id needs to be the same as NRIC")
        
hour = float(input("Enter Total Teaching Hour: "))
lecturer_1 = Lecturer(name, nric, staff_id)
lecturer_1.set_total_teaching_hour(hour)


name = input("Enter Student Name: ")
nric = input("Enter Student NRIC: ")
admin_no = input("Enter Student Admin No: ")

# Use different approaches to validate test and exam mark
while True:
    test_mark = float(input("Enter Test mark: "))
    if test_mark < 0 or test_mark > 100:
        print("Test marks must be between 0 to 100 (inclusive)")
    else:
        break

while True:
    exam_mark = float(input("Enter Exam mark: "))
    if exam_mark < 0 or exam_mark > 100:
        print("Exam marks must be between 0 to 100 (inclusive)")
    else:
        break

student_1 = Student(name, nric, admin_no)
student_1.set_test_mark(test_mark)
student_1.set_exam_mark(exam_mark)

print(lecturer_1)
print(student_1)

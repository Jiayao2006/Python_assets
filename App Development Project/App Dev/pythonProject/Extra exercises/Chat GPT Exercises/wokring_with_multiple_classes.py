class Student:
    def __init__(self, name, age):
        self.__student = name
        self.__age = age

    def __str__(self):
        return f"Name: {self.__student}, Age: {self.__age}"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        if not self.students:
            print(f"No students enrolled in {self.course_name}.")
        else:
            print(f"Students enrolled in {self.course_name}")
            for student in self.students:
                print(student)


# Create some Student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Create a Course object
course = Course("Python Programming")

# Add students to the course
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# Print the list of enrolled students
course.print_students()

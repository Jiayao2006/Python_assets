from student import Student
from person import Person

class Lecturer(Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_teaching_hour = 0

    def get_staff_id(self):
        return self.__staff_id

    def get_total_teaching_hour(self):
        return self.__total_teaching_hour

    def set_staff_id(self, staffid):
        self.__staff_id = staffid

    def set_total_teaching_hour(self, teachingHour):
        self.__total_teaching_hour = teachingHour

    def compute_salary(self):
        salary = self.get_total_teaching_hour() * 90
        return salary

    def __str__(self):
        return f"{self.get_name()}, Staff ID: {self.get_staff_id()} earns ${self.compute_salary()}"

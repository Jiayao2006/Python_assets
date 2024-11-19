from Person import *


class Lecturer(Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_teaching_hour = 0

    def get_staff_id(self):
        return self.__staff_id

    def get_total_teaching_hour(self):
        return self.__total_teaching_hour
        
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_total_teaching_hour(self, total_teaching_hr):
        self.__total_teaching_hour = total_teaching_hr

    def compute_salary(self):
        return self.__total_teaching_hour * 90

    def __str__(self):
        s = f"{self.get_name()}, Staff Id: {self.get_staff_id()} earns ${self.compute_salary():.2f}"
        return s

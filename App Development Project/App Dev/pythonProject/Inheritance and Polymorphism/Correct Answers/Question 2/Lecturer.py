from Person import *


class Lecturer(Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_Id = staff_id
        self.__total_teaching_hour = 0

    def get_staff_id(self):
        return self.__staff_Id

    def set_staff_id(self, staff_id):
        self.__staff_Id = staff_id

    def get_total_teaching_hour(self):
        return self.__total_teaching_hour

    def set_total_teaching_hour(self, total_teaching_hour):
        self.__total_teaching_hour = total_teaching_hour

    def compute_salary(self):
        return self.__total_teaching_hour * 90

    def __str__(self):
        return f"{self.get_name()}, Staff Id: {self.__staff_Id}, earns ${self.compute_salary():.2f}"

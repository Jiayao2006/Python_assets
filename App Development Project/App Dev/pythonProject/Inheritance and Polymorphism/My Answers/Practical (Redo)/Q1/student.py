from person import Person

class Student(Person):
    def __init__(self, name, nric, admin_no):
        Person.__init__(self, name, nric)
        self.__admin_no = admin_no
        self.__test_mark = 0
        self.__exam_mark = 0

    def get_admin_no(self):
        return self.__admin_no

    def get_test_mark(self):
        return self.__test_mark

    def get_exam_mark(self):
        return self.__exam_mark

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def set_test_mark(self, test_mark):
        self.__test_mark = test_mark

    def set_exam_mark(self, exam_mark):
        self.__exam_mark = exam_mark

    def compute_final_mark(self):
        return (self.get_exam_mark() + self.get_test_mark()) * 0.5

    def __str__(self):
        return f"{self.get_name()}, Admin No: {self.get_admin_no()}, final mark is {self.compute_final_mark()}"
from question1 import Person


class Student(Person):
    def __init__(self, nric, name, test_mark, exam_mark):
        Person.__init__(self, nric, name)
        self.__test_mark = test_mark
        self.__exam_mark = exam_mark

    def get_test_mark(self):
        return self.__test_mark

    def get_exam_mark(self):
        return self.__exam_mark

    def set_test_mark(self, mark):
        if 0 <= mark <= 100:
            self.__test_mark = mark
        else:
            print("Exam marks must be between 0 to 100 (inclusive)")

    def set_exam_mark(self, mark):
        if 0 <= mark <= 100:
            self.__exam_mark = mark
        else:
            print("Test marks must be between 0 to 100 (inclusive)")

    def compute_final_mark(self):
        return 0.5 * (self.__test_mark + self.__exam_mark)

    def __str__(self):
        return (f"Name: {self.get_name()}\nNRIC: {self.get_nric()}\nTest Score: {self.get_test_mark()}\n"
                f"Exam Score: {self.get_exam_mark()}\nFinal Mark: {self.compute_final_mark()}")
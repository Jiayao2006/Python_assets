class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.__name = name

    def display_employee_info(self):
        print(f"Company: {Employee.company_name}, Employee: {self.__name}")


employee1 = Employee("Alice")
employee2 = Employee("Bob")
employee1.display_employee_info()
employee2.display_employee_info()
import shelve

class Questions:
    def __init__(self, id, description, answer):
        self.__id = id
        self.__description = description
        self.__answer = answer

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_answer(self):
        return self.__answer

    def set_id(self, id):
        self.__id = id

    def set_description(self, description):
        self.__description = description

    def set_answer(self, answer):
        self.__answer = answer

def menu():
    while True:
        print("Select the program (1-3) to run: ")
        print("1. Add a Question")
        print("2. Display a Question (by id)")
        print("3. Quit the program")

        try:
            val = int(input("Enter your command (1-3): "))
        except ValueError:
            val = 3

        if val == 1:
            add()
        elif val == 2:
            display()
        else:
            print("End of program")
            break

def add():
    try:
        id = input("Enter question id: ")
        description = input("Enter question description: ")
        answer = input("Enter question answer: ")
        question = Questions(id, description, answer)
        with shelve.open("question_inventory") as db:
            db[id] = question
            print("A question is added to file")
    except:
        print("Unknown error occurred")


def display():
    try:
        id = input("Enter the question id to display: ")
        with shelve.open("question_inventory") as db:
            if id in db:
                question = db[id]
                print(f"Question ID: {question.get_id()}, Description: {question.get_description()}, Answer: {question.get_answer()}")
            else:
                raise KeyError
    except KeyError:
        print("No such question")
    except:
        print("Unknown error occurred")

if __name__ == '__main__':
    menu()
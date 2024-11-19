import shelve

# Define the Question class
class Question:
    def __init__(self, question_id, description, answer):
        self.id = question_id
        self.description = description
        self.answer = answer

    def __str__(self):
        return f"Question id: {self.id}, Description: {self.description}, Answer: {self.answer}"

# Function to display the menu
def menu():
    while True:
        print("\nSelect the program (1-3) to run:")
        print("1. Add a Question")
        print("2. Display a Question (by id)")
        print("3. Quit the program")

        try:
            val = int(input("Enter your command (1-3): "))
        except ValueError:
            val = 3  # Default to quitting if invalid input

        if val == 1:
            add()
        elif val == 2:
            display()
        else:
            print("End of program")
            break

# Function to add a question
def add():
    try:
        question_id = input("Enter question id: ")
        description = input("Enter question description: ")
        answer = input("Enter question answer: ")

        # Create a Question object
        question = Question(question_id, description, answer)

        # Store the Question object in the shelve
        with shelve.open("questions_db") as db:
            db[question_id] = question
            print("A question added to file")
    except Exception as e:
        print(f"Error adding question: {e}")

# Function to display a question by id
def display():
    try:
        question_id = input("Enter the question id to display: ")

        # Retrieve the question from the shelve
        with shelve.open("questions_db") as db:
            if question_id in db:
                print(db[question_id])
            else:
                print("No such question")
    except Exception as e:
        print(f"Error displaying question: {e}")

# Run the menu
menu()

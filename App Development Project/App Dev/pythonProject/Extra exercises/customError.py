10
class CustomError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.__message = message

    def __str__(self):
        return f"{self.__message}"

try:
    num = int(input("Enter a number"))
    if num < 0:
        raise CustomError("Number Less than 0")
    elif num > 9:
        raise CustomError("Number is more than 9")
except CustomError as e:
    print(e)

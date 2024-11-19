import shelve


def store():
    with shelve.open("my_shelve") as db:
        db["name"] = "Alice"
        db["age"] = 25
        db["city"] = "New York"

def retrieve():
    with shelve.open("my_shelve") as db:
        print(db.get("name"))
        print(db.get("age"))
        if "city" in db:
            print(db.get("city"))

if __name__ == '__main__':
    store()
    retrieve()
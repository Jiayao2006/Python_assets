class ShoppingCart:
    items = {}

    def __init__(self, id, name):
        self.__cart_id = id
        self.__customer_name = name
        self.__discount_code = "SAVE10"
        self.__give_discount = "No"

    def get_cart_id(self):
        return self.__cart_id

    def get_customer_name(self):
        return self.__customer_name

    def set_cart_id(self, id):
        self.__cart_id =  id

    def set_customer_name(self, name):
        self.__customer_name = name

    def add_item(self, item_name, price, quantity):
        ShoppingCart.items[item_name] = [price, quantity]

    def remove_item(self, item_name):
        try:
            if item_name in ShoppingCart.items:
                del ShoppingCart.items[item_name]

            else:
                raise KeyError

        except KeyError:
            print("Item not in shopping cart.")

    def apply_discount(self, code):
        if code == self.__discount_code:
            self.__give_discount = "Yes"
        else:
            print("Invalid code")

    def get_total(self):
        total = 0
        for value in ShoppingCart.items.values():
            total += (value[0] * value[1])

        if self.__give_discount == "Yes":
            total = total * 0.9
        return total








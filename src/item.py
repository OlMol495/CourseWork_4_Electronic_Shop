import csv

class Item:
    """Класс для общих данных по товару в магазине: название, цена, количество"""
    pay_rate = 0.8
    all = []
    csv_file = "../src/items.csv"

    def __init__(self, name, price, amount):
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)
        #self.all.append({"название": self.name, "цена": self.price, "количество": self.amount})

    def __str__(self):
        return f"Item('{self.__name}', {self.price}, {self.amount})"

    def __repr__(self):
        return f'{self.__name}'

    def calculate_total_price(self):
        """return total price of all items of the category"""
        return self.price * self.amount

    def apply_discount(self):
        """return discounted price of one item"""
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10] + "*"

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        cls.all.clear()
        with open(csv_file, encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = row["price"]
                amount = row["quantity"]
                cls(name, price, amount)


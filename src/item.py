import csv


class Item:
    """Класс для общих данных по товару в магазине:
    название, цена, количество"""
    pay_rate = 0.8
    all = []
    csv_file = "../src/item.csv"

    def __init__(self, name: str, price: float, amount: int):
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __str__(self) -> str:
        return f'{self.__name}'

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}('{self.__name}',"
                f" {self.price}, {self.amount})")

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
        """shortens name of item to 10 symbols"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10] + "*"

    @staticmethod
    def string_to_number(str_num):
        """transfer number from string to number as int"""
        return int(float(str_num))

    @classmethod
    def instantiate_from_csv(cls):
        """creates dict from csv file data, raises errors
             if no file or data corrupted"""
        cls.all.clear()
        try:
            with open(cls.csv_file, encoding='cp1251') as file:
                reader = csv.DictReader(file)
                if reader.fieldnames != ["name", "price", "quantity"]:
                    raise InstantiateCSVError
                for row in reader:
                    name = str(row["name"])
                    price = float(row["price"])
                    amount = int(row["quantity"])
                    cls(name, price, amount)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    def __add__(self, other):
        """складываем два экземпляра по количеству товара"""
        if not isinstance(other, Item):
            raise ValueError("Нельзя складывать экземпляры, "
                             "не принадлежащие классам Item или Phone")
        return self.amount + other.amount


class InstantiateCSVError(Exception):
    """class for exception of file data corruption"""
    def __init__(self, *args):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message

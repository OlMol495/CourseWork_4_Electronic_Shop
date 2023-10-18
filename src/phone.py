from src.item import Item

class Phone(Item):
    def __init__(self, name, price, amount, number_of_sim):
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.amount}, {self.number_of_sim})"






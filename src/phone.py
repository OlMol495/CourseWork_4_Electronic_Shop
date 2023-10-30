from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float,
                 amount: int = 0, number_of_sim: int = 1) -> None:
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}('{self.name}', "
                f"{self.price}, {self.amount}, {self.number_of_sim})")

    @property
    def number_of_sim(self):
        """getter for number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        """sets that number of sims should integer and bigger than zero"""
        if not isinstance(number, int) or number < 1:
            raise ValueError("Количество сим-карт должно быть "
                             "целым числом и больше нуля")
        self.__number_of_sim = number

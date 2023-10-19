from src.item import Item

class Phone(Item):
    def __init__(self, name, price, amount, number_of_sim):
        super().__init__(name, price, amount)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.amount}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """getter for number_of_sim"""
        return self.number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """sets that number of sims should integer and bigger than zero"""
        if isinstance(number, int) and number > 0:
            self.number_of_sim = number
        raise ValueError("Количество сим-карт должно быть целым числом и больше нуля")











from src.item import Item

class KeyboardLanguage:
    """Mixin class to establish keyboard language and change it between RU and EN"""
    eng_key = "EN"
    rus_key = "RU"

    def change_lang(self):
        """method to change keyboard between RU and EN"""
        if self.language == self.eng_key:
            self.language = self.rus_key

        else:
            self.language = self.eng_key


class Keyboard(Item, KeyboardLanguage):
    """class for keyboard inherits from Item and Mixin class KeyboardLanguage """
    def __init__(self, name, price, amount, language="EN"):
        super().__init__(name, price, amount)
        self.language = language




from src.item import Item
from src.phone import Phone

test_item = Item("Watches", 10000, 5) #test exemplar
test_item1 = Item("Laptop", 60000, 3)
test_phone1 = Phone("LG", 30000, 3, 2)
test_phone2 = Phone("Xaomi", 40000, 5, 4)

def test_phone_str():
    assert test_phone1.__str__() == "LG"

def test_phone_repr():
    assert test_phone1.__repr__() == "Phone('LG', 30000, 3, 2)"




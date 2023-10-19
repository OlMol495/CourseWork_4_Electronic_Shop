from src.item import Item
from src.phone import Phone
import pytest


test_item = Item("Watches", 10000, 5) #test exemplar
test_item1 = Item("Laptop", 60000, 3)
test_phone1 = Phone("LG", 30000, 3, 2)
test_phone2 = Phone("Xaomi", 40000, 5, 4)

def test_phone_str():
    assert test_phone1.__str__() == "LG"

def test_phone_repr():
    assert test_phone1.__repr__() == "Phone('LG', 30000, 3, 2)"

def test_add_dc():
    """тест на сложение двух экземпляров по количеству товара"""
    assert test_item + test_phone1 == 8

def test_add_error():
    """тест на ошибку, если складываются не экземпляры нужных классов"""
    with pytest.raises(ValueError) as err:
        test_item + 2000
        assert str(err.value) == "Нельзя складывать экземпляры, не принадлежащие классам Item или Phone"

def test_setter_number_of_sim():
    """тест на ошибку, если количество симок указано неверно"""
    with pytest.raises(ValueError) as err:
        test_phone1.number_of_sim = 1
        assert str(err.value) == "Количество сим-карт должно быть целым числом и больше нуля"

def test_setter_number_of_sim_ins():
    """тест на ошибку, когда количество симок указано не как целое число"""
    with pytest.raises(ValueError) as err:
        test_phone1.number_of_sim = "2"
        assert str(err.value) == "Количество сим-карт должно быть целым числом и больше нуля"







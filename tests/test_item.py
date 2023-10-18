"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import csv
import os
import pytest

test_item = Item("Watches", 10000, 5) #test exemplar
test_item1 = Item("Laptop", 60000, 3)
test_phone1 = Phone("LG", 30000, 3, 2)
test_phone2 = Phone("Xaomi", 40000, 5, 4)

def test_str():
    assert test_item.__str__() == 'Watches'


def test_repr():
    assert test_item.__repr__() == "Item('Watches', 10000, 5)"


def test_calculate_total_price():
    """checking calculate_total_price"""
    assert test_item.calculate_total_price() == 50000


def test_apply_discount():
    """checking price with discount"""
    test_item.apply_discount()
    assert test_item.price == 8000

def test_name():
    """checking setter name"""
    test_item1.name = "Smartphone"
    assert test_item1.__repr__() == "Item('Smartphone', 60000, 3)"

def test_long_name():
    """checking setter name for names longer than 10 characters"""
    test_item1.name = "Supersmartphone"
    assert test_item1.__repr__() == "Item('Supersmart*', 60000, 3)"

def test_string_to_number():
    """checking that func return int from string with digits"""
    assert Item.string_to_number("8000") == 8000
    assert Item.string_to_number("8000.0") == 8000
    assert Item.string_to_number("8000.5") == 8000

def test_instantiate_from_csv_len():
    """checking that function creates list of right length"""
    Item.instantiate_from_csv("../src/items.csv")
    assert len(Item.all) == 5






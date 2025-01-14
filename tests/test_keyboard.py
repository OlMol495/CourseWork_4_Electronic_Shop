from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_str():
    """testing __str__ for Keyboard class"""
    assert str(kb) == "Dark Project KD87A"


def test_original_lang():
    """testing that original keyboard language is EN"""
    assert kb.language == "EN"


def test_change_lang():
    """testing and language changes from EN to RU"""
    kb.change_lang()
    assert kb.language == "RU"


def test_change_lang_EN():
    kb.change_lang()
    kb.change_lang()
    assert kb.language == "EN"


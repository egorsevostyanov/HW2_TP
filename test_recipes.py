import pytest

from hw2 import Ingredient

def test_ingredient1():
    ing = Ingredient("Мука", 100, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 100
    assert ing.unit == "г"

def test_ingredient2():
    ing = Ingredient("Мука", 100, "г")
    assert str(ing) == "Мука: 100.0 г"

def test_ingredient3():
    ing1 = Ingredient("Мука", 100, "г")
    ing2 = Ingredient("Мука", 200, "г")
    ing3 = Ingredient("b", 100, "г")
    ing4 = Ingredient("b", 100, "мл")
    assert ing1 == ing2
    assert ing1 != ing3
    assert ing4 != ing3
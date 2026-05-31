import pytest

from hw2 import Ingredient, Recipe

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

def test_recipe1():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    assert r.title == "c"
    assert r.ingredients == [ing1, ing2]

def test_recipe2():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    ing3 = Ingredient("d", 50, "г")
    r = Recipe("c", [ing1, ing2])
    r.add_ingredient(ing3)
    assert r.ingredients == [ing1, ing2, ing3]

def test_recipe3():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    r.add_ingredient(Ingredient("a", 50, "г"))
    assert r.ingredients == [Ingredient("a", 150, "г"), ing2]

def test_recipe4():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    r2 = r.scale(2)
    assert r.ingredients == [ing1, ing2]
    assert r2.title == "c"
    assert r2.ingredients == [Ingredient("a", 200, "г"), Ingredient("b", 400, "г")]

def test_recipe5():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    with pytest.raises(ValueError):
        r.scale(-1)

def test_recipe6():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("a", 200, "г")
    r = Recipe("c", [ing1])
    r.add_ingredient(ing2)
    assert len(r) == 1
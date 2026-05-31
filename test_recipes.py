import pytest

from hw2 import Ingredient, Recipe, ShoppingList

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

def test_shoppinglist1():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    sl = ShoppingList()
    sl.add_recipe(r, 1)
    assert sl._items == [(ing1, "c"), (ing2, "c")]

def test_shoppinglist2():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(r, -1)

def test_shoppinglist3():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    sl = ShoppingList()
    sl.add_recipe(r, 2)
    sl.remove_recipe("d")
    sl.remove_recipe("c")
    assert sl._items == []

def test_shoppinglist4():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    sl = ShoppingList()
    sl.add_recipe(r, 2)
    assert sl.get_list() == [Ingredient("a", 200, "г"), Ingredient("b", 400, "г")]

def test_shoppinglist5():
    ing1 = Ingredient("a", 100, "г")
    ing2 = Ingredient("b", 200, "г")
    r = Recipe("c", [ing1, ing2])
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(r, 2)
    sl2.add_recipe(r, 3)
    sl3 = sl1 + sl2
    assert sl3.get_list() == [Ingredient("a", 500, "г"), Ingredient("b", 1000, "г")]
    assert sl1.get_list() == [Ingredient("a", 200, "г"), Ingredient("b", 400, "г")]
    assert sl2.get_list() == [Ingredient("a", 300, "г"), Ingredient("b", 600, "г")]

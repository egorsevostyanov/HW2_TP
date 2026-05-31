class Ingredient:
    def __init__(self, name : str, quantity : float, unit : str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return NotImplemented
        return (self.name == other.name and self.unit == other.unit)


class Recipe:
    def __init__(self, title : str, ingredients : list):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient : Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio : float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должен быть числом больше нуля")
        ing = []
        for i in self.ingredients:
            ing.append(Ingredient(i.name, i.quantity * ratio, i.unit))
        return Recipe(self.title, ing)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f"{self.title}: {', '.join(str(i) for i in self.ingredients)}"
    
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        sc = recipe.scale(portions);
        for i in sc.ingredients:
            self._items.append((i, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [i for i in self._items if i[1] != title]

    def get_list(self):
        mp = {}
        for i, j in self._items:
            k = (i.name, i.unit)
            mp[k] = mp.get(k, 0)+i.quantity
        ans = [Ingredient(name, quantity, unit) for (name, unit), quantity in mp.items()]
        ans.sort(key=lambda x: x.name)
        return ans
    
    def __add__(self, other: 'ShoppingList'):
        list = ShoppingList()
        list._items = self._items.copy()+other._items.copy()
        return list
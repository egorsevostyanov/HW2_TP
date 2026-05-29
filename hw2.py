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
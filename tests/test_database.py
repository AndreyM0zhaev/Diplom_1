from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3, "Список булочек пустой"

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) > 0, "Список ингредиентов пустой"
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient), "Элемент списка не является ингредиентом"

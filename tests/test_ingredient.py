from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientTypes
import pytest



class TestIngredient:

    def test_get_ingredient_price(self):
        ingredient = Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        assert ingredient.get_price() == 90, "Неверная цена ингредиента"


    def test_get_ingredient_name(self):
        ingredient = Ingredient(IngredientTypes.INGREDIENT_TYPE_FILLING, "Сыр с астероидной плесенью", 4142)
        assert ingredient.get_name() == "Сыр с астероидной плесенью", "Неверное название ингредиента"


    @pytest.mark.parametrize(
        'type, name, price',
        [
            ['Соус фирменный Space Sauce', 80, IngredientTypes.INGREDIENT_TYPE_SAUCE],
            ['Филе Люминесцентного тетраодонтимформа', 988, IngredientTypes.INGREDIENT_TYPE_FILLING]
        ]
    )

    def test_get_ingredient_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

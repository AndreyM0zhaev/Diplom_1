from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import IngredientTypes

class TestIngredient:

    def test_get_ingredient_price(self):
        ingredient = Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        assert ingredient.get_price() == 90, "Неверная цена ингредиента"

    def test_get_ingredient_name(self):
        ingredient = Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90)
        assert ingredient.get_name() == "Соус Spicy-X", "Неверное название ингредиента"



from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import IngredientTypes



class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger.set_buns(bun)
        assert burger.bun == bun, "Булочка не была установлена"

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock('sauce', 'жгучий перчик', 88)
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients, "Ингредиент не был добавлен"


from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import IngredientTypes
from praktikum.database import Database



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


    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient0 = Mock('sauce', 'жгучий перчик', 88)
        mock_ingredient1 = Mock('filling', 'эктоплазма', 111)
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert mock_ingredient0 not in burger.ingredients, "Ингредиент не был удален"
        assert mock_ingredient1 in burger.ingredients, "Был удален необходимый ингредиент"


    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient0 = Mock('sauce', 'жгучий перчик', 88)
        mock_ingredient1 = Mock('filling', 'эктоплазма', 111)
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient1, "Первый ингредиент не на своем месте"
        assert burger.ingredients[1] == mock_ingredient0, "Ингредиент не был перемещен"
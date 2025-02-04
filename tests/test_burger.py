from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun



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


    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 988
        mock_ingredient0 = Mock()
        mock_ingredient0.get_price.return_value = 88
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 111
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)
        assert burger.get_price() == 2175, "Неверная стоимость бургера"


    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Флюоресцентная булка R2-D3"
        mock_bun.get_price.return_value = 988

        mock_ingredient0 = Mock()
        mock_ingredient0.get_type.return_value = "sauce"
        mock_ingredient0.get_name.return_value = "жгучий перчик"
        mock_ingredient0.get_price.return_value = 88

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = "filling"
        mock_ingredient1.get_name.return_value = "эктоплазма"
        mock_ingredient1.get_price.return_value = 111

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient0)
        burger.add_ingredient(mock_ingredient1)

        expected_receipt = (
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "= sauce жгучий перчик =\n"
            "= filling эктоплазма =\n"
            "(==== Флюоресцентная булка R2-D3 ====)\n\n"
            "Price: 2175"
        )

        assert burger.get_receipt() == expected_receipt, "Ошибка в чеке"
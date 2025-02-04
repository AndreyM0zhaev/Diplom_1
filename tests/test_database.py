from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3, "Список булочек пустой"



from praktikum.bun import Bun



class TestBun:

    def test_get_bun_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3', "Неверное название"


    def test_get_bun_price(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255, "Неверная цена"

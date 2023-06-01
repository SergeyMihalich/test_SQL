import pytest

from Base.base import Base
from Resources.data import quantity


# выполнение проверок по каждому кораблю, сам тест описан на странице 'Base'
@pytest.mark.parametrize("num", range(1, quantity['ships'] + 1))
class TestShip(Base):
    # проверка характеристик оружия на корабле
    def test_select_weapons(self, database, num):
        select_weapons = 'SELECT ship, w.* FROM ships s join weapons w on s.weapon = w.weapon WHERE ship == :value'
        self.components_checking(database, num, select_weapons, 'weapon', 'weapons')

    # проверка характеристик корпуса на корабле
    def test_select_hulls(self, database, num):
        select_hulls = 'SELECT ship, h.* FROM ships s join hulls h on s.hull = h.hull WHERE ship == :value'
        self.components_checking(database, num, select_hulls, 'hull', 'hulls')

    # проверка характеристик двигателя на корабле
    def test_select_engines(self, database, num):
        select_engines = 'SELECT ship, e.* FROM ships s join engines e on s.engine = e.engine WHERE ship == :value'
        self.components_checking(database, num, select_engines, 'engine', 'engines')

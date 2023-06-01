import pytest
import sqlite3

from Resources.data import quantity
from DB.dataGeneration import ship_data_generation, data_generation
from DB.dbCreation import creation_table
from DB.dbUpdate import data_change


# создал файл CSV для себя, чтобы проще было читать результаты тестов, перед каждой сессией файл чиститься
@pytest.fixture(scope='session')
def setup_before_tests():
    error_file = 'error_file.csv'
    with open(error_file, 'w', newline='') as file:
        file.truncate()


# перед каждой сессий выполняется соединение с основной БД, если ее нет то создается новая;
# происходит заполнение;
# создается соединение с временной БД;
# временная БД является копией основной;
# во временной БД изменяются значения
# cursor - основой БД и new_cursor - временной бд передаются по фикстуре в тесты
@pytest.fixture(scope='session')
def database():
    with sqlite3.connect('baseDB.db') as db:
        db.row_factory = sqlite3.Row
        cursor = creation_table(db.cursor())
        completion(cursor)

        db.commit()

        with sqlite3.connect(':memory:') as ndb:
            db.backup(ndb)
            ndb.row_factory = sqlite3.Row
            new_cursor = ndb.cursor()
            db_change(new_cursor)
    yield cursor, new_cursor


# генерация значений в основной БД если она пуста
def completion(cursor):
    ship_data_generation('ships', quantity['weapons'], quantity['hulls'], quantity['engines'], cursor)
    data_generation('weapons', cursor)
    data_generation('hulls', cursor)
    data_generation('engines', cursor)


# изменение значений во временной БД
def db_change(cursor):
    for num in range(1, quantity['ships'] + 1):
        data_change(cursor, num)

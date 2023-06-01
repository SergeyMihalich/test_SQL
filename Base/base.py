import csv
from Resources.data import table_columns


class Base:

    # проверка на соответствие компонента установленного на корабль в основной и временной БД
    # проверка на соответствие характеристик установленного на корабль компонента в основной и временной БД
    def components_checking(self, database, num, select_db, component, table):
        cursor, new_cursor = database
        print()
        value = f'ship-{num}'

        cursor.execute(select_db, {"value": value})
        res_1 = cursor.fetchone()
        # print(*res_1)

        new_cursor.execute(select_db, {"value": value})
        res_2 = new_cursor.fetchone()
        # print(*res_2)

        # запись ошибок делал для себя для упрощения проверки

        error_file = 'error_file.csv'
        if res_1[component] != res_2[component]:
            with open(error_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [f'{value}, {res_1[component]}\n    expected {res_2[component]}, was {res_1[component]}'])

        # проверка компонента установленного на корабль

        assert res_1[component] == res_2[
            component], f'{value}, {res_1[component]}\n    expected {res_2[component]}, was {res_1[component]}'

        val_assert = f'{value}, {res_1[component]}'
        flag = True
        for i in table_columns[table][1:]:
            i = i.replace('`', '')
            if res_1[i] != res_2[i]:
                val_assert += f'\n    {i}: expected {res_2[i]}, was {res_1[i]}'
                flag = False

        # запись ошибок делал для себя для упрощения проверки

        error_file = 'error_file.csv'
        if not flag:
            with open(error_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([val_assert])

        # проверка характеристик компонента установленного на корабль

        assert flag, f'{val_assert}'


if __name__ == '__main__':
    pass

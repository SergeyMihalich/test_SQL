from random import randint

from Resources.data import table_columns, quantity


def filling(fkey, n):
    a = []
    for _ in range(n):
        a.append(randint(1, 20))
    return (fkey, *a)

# генерация рандомных значений и заполнение ими таблицы 'ship' если она пуста
def ship_data_generation(table, weapon, hull, engine, cursor):
    cursor.execute('''SELECT COUNT(*) FROM ships''')
    result = cursor.fetchone()
    if result[0] == 0:
        ship = [(f'ship-{i + 1}', f'weapon-{randint(1, weapon)}', f'hull-{randint(1, hull)}',
                 f'engine-{randint(1, engine)}')
                for i in range(quantity[table])]
        cursor.executemany(
            'INSERT INTO ships(ship, weapon, hull, engine) VALUES(?, ?, ?, ?)', ship
        )

# генерация рандомных значений и заполнение ими таблиц 'weapon', 'hull', 'engine' если таблица пуста
def data_generation(table, cursor):
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    result = cursor.fetchone()
    if result[0] == 0:
        len_col = len(table_columns[table])
        weapon = [filling(f'{table_columns[table][0]}-{i + 1}', len_col - 1) for i in range(quantity[table])]
        placeholders = ', '.join(['?' for _ in range(len_col)])
        query = f'INSERT INTO {table} VALUES({placeholders})'
        cursor.executemany(query, weapon)


if __name__ == '__main__':
    pass
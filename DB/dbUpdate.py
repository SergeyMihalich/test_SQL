from random import randint
from Resources.data import table_columns, quantity


# выбор рандомной колонки таблицы
def rand_column(table):
    rand_index = randint(1, len(table_columns[table]) - 1)
    result = table_columns[table][rand_index]
    return result


# изменение рандомного компонента корабля и одного рандомного значения компонента из установленных на корабль
# изменение значений компонентов происходит после смены компонента корабля на новый
def data_change(cursor, num):
    value = f'ship-{num}'
    column = rand_column('ships')
    random_value = f'{column}-{randint(1, quantity[f"{column}s"])}'
    query = f'UPDATE ships SET {column} = ? WHERE ship = ?'
    cursor.execute(query, (random_value, value))

    for table in list(quantity.keys())[1:]:
        print(table)
        query = f"UPDATE {table} SET {rand_column(table)} = :value_2 WHERE {table_columns[table][0]} IN (SELECT {table_columns[table][0]} FROM ships WHERE ship = :value)"
        print(query)
        cursor.execute(query, {"value_2": randint(1, 20),
                               "value": value})


if __name__ == '__main__':
    pass

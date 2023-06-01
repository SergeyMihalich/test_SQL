
# создание таблиц основной БД если таблиц не существует
def creation_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ships(
        ship text PRIMARY KEY,
        weapon text,
        hull text,
        engine text,
        foreign key (weapon) references weapons(weapon),
        foreign key (hull) references hulls(hull),
        foreign key (engine) references engines(engine)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS weapons(
        weapon text PRIMARY KEY,
        `reload speed` integer,
        `rotational speed` integer,
        diameter integer,
        `power volley` integer,
        `count` integer
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS hulls(
        hull text PRIMARY KEY,
        armor integer,
        `type` integer,
        capacity integer
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS engines(
        engine text PRIMARY KEY,
        capacity integer,
        `type` integer
    )''')
    return cursor
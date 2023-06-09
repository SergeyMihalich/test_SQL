## Цели задания

1. Написать python-скрипт, создающий SQLite базу по указанной схеме.
Primary key – текстовое поле weapon / ship / hull / engine соответственно


2. Создать скрипт, который будет рандомно заполнять значения в созданной базе. Вполне
сгодятся названия: Ship-1, Ship-2, Weapon-1 и т. д,


   Количество записей для каждой таблицы:<br>
   ships: 200<br>
   weapons: 20<br>
   hulls: 5<br>
   engines: 6<br>

   Диапазон значений для целочисленных параметров: 1-20

3. Создать session-scope фикстуру, которая получает текущее состояние базы данных и создает временную новую базу, в которой рандомизируются значения:
   
   - Для каждого корабля меняется на случайный один из компонентов: корпус, орудие
или двигатель
   - В каждом компоненте меняется один из случайно выбранных параметров на
случайное значение из допустимого диапазона (см. выше)
   
4. Написать автотесты, сравнивающие данные из исходной базы с полученной
рандомизированной:
   - Для каждого корабля должно быть 3 теста, проверяющие его орудие, корпус и
двигатель.
   - Тест должен падать с assert:
      - Когда значение параметра компонента не соответствует тому, что было до
запуска рандомизатора.<br>
      Пример вывода:    
     
         - Ship-2, weapon-1   
            - reload speed: expected 1, was 2   
            - diameter: expected 2, was 3    
         
         - Ship-2, hull-3  
            - type: expected 1, was 2  
            - Ship-3, engine-6    
            - power: expected 22, was 13   

---

## Требования к выполненному заданию

- Версия Python – 3.8
- Тесты должны быть написаны с использованием фрейморка pytest
- В качестве параметризации использовать pytest.mark.parametrize или хук pytest_generate_tests.
- В результате прогона должно получиться 600 тестов.
- В результате выполнения задания должно быть по крайней мере следующее:
   - Скрипт, создающий и заполняющий исходную базу данных
   - Python-модуль, содержащий тесты
   - (Опционально) conftest.py, содержащий фикстуры и хуки
- Стиль кода – PEP8.

___

### команды зля запуска

Сохраните обновленный Dockerfile и выполните команду для сборки Docker-образа:

```
docker build -t my_project:latest .
```

После успешного завершения сборки можно запустить контейнер для выполнения тестов:

```
docker run --rm -it my_project:latest
```


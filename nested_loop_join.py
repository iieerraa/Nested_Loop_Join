def join(table1, table2):  # основная функция для Nested loop join, принимает две таблицы List[Tuple]
    table = []  # инициализация итоговой таблицы
    for tuple1 in table1:  # цикл для каждой строчки первой таблицы
        for tuple2 in table2:  # цикл для каждой строчки второй таблицы
            if condition_callback(tuple1, tuple2):  # принимаем результат функции сравнения строк таблиц
                table.append(select_columns_callback(tuple1, tuple2))  # построение итоговой таблицы

    return order_comparator_callback(table)  # возврат итоговой отсортированной таблицы


def condition_callback(tuple1, tuple2):  # функция сравнения первой и второй таблицы построчно
    return tuple1[1] == tuple2[0]  # сравнение по индексу элемента в строке


def select_columns_callback(tuple1, tuple2):  # функция соединения строк первой и второй таблицы
    return tuple1 + tuple2  # соединение двух строк


def order_comparator_callback(table):  # сортировка таблицы по индексу элемента
    table.sort(key=lambda x: x[1])  # сортировка списка по индексу элемента кортежа
    return table  # возврат отсортированной таблицы


# первая таблица List[Tuple]
t1 = [
    (1, "a"),
    (2, "b"),
    (3, "c"),
    (4, "d")
]
# вторая таблица List[Tuple]
t2 = [
    ("a", "abra"),
    ("b", "babra"),
    ("c", "cabra"),
    ("d", "dabra"),
    ("e", "eureka"),
    ("f", "furia")
]

print(join(t1, t2))  # вывод итогового результата

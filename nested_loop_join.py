"""Модуль Nested loop join"""
from typing import List, Tuple, Callable


def __condition_callback(tuple1: Tuple, tuple2: Tuple):  # функция сравнения первой и второй таблицы построчно
    """Сравнить отдельные строки таблицы по индексу элемента

    :param tuple1: - принимает отделюную строку Tuple таблицы table1
    :param tuple2: - принимает отдельную строку Tuple таблицы table2
    :return: - bool (True/False) при сравнении строк
    """
    return tuple1[1] == tuple2[0]  # сравнение по индексу элемента в строке


def __select_columns_callback(tuple1: Tuple, tuple2: Tuple):  # функция соединения строк первой и второй таблицы
    """Соединить строки таблицы

    :param tuple1: - принимает отделюную строку Tuple таблицы table1
    :param tuple2: - принимает отдельную строку Tuple таблицы table2
    :return: - соединение строк tuple1 и tuple2
    """
    return tuple1 + tuple2  # соединение двух строк


def __order_comparator_callback(table: List[Tuple]):  # сортировка таблицы по индексу элемента
    """Отсортировать таблицу по индексу элемента

    :param table: - принимает таблицу List[Tuple] для сортировки
    :return: - возврат table отсортированного по индексу элемента кортежа
    """
    table.sort(key=lambda x: x[1])  # сортировка списка по индексу элемента кортежа
    return table  # возврат отсортированной таблицы


def join(
        table1: List[Tuple],
        table2: List[Tuple],
        join_callback: Callable[[Tuple, Tuple], bool] = __condition_callback,
        select_callback: Callable[[Tuple, Tuple], Tuple] = __select_columns_callback,
        order_callback: Callable[[List[Tuple]], List[Tuple]] = __order_comparator_callback,
        is_left_join: bool = False,):
    """ создать новую таблицу через алгоритм join

    :param table1: - принимает первую таблицу List[Tuple]
    :param table2: - принимает вторую таблицу List[Tuple]
    :param join_callback: - принимает функцию для сравнения таблиц
    :param select_callback: - принимает функцию соединения таблиц
    :param order_callback: - принимает функцию сортировки итоговой таблицы
    :param is_left_join: -
    :return: - итоговая таблица table с результатом соединения двух входящих таблиц

    пример первой таблицы
    t1 = [
    (1, "a"),
    (2, "b"),
    (3, "c"),
    (4, "d")]
    пример второй таблицы
    t2 = [
    ("a", "abra"),
    ("b", "babra"),
    ("c", "cabra"),
    ("d", "dabra"),
    ("e", "eureka"),
    ("f", "furia")]
    результатом алгоритма по умолчанию будет итоговая таблица:
    table = [
    (1, "a", "a", "abra"),
    (2, "b", "b", "babra"),
    (3, "c", "c", "cabra"),
    (4, "d", "d", "dabra")]
    """
    table: List[Tuple] = []  # инициализация итоговой таблицы
    for tuple1 in table1:  # цикл для каждой строчки первой таблицы
        for tuple2 in table2:  # цикл для каждой строчки второй таблицы
            if join_callback(tuple1, tuple2):  # принимаем результат функции сравнения строк таблиц
                table.append(select_callback(tuple1, tuple2))  # построение итоговой таблицы
    return order_callback(table)  # возврат итоговой отсортированной таблицы


if __name__ == '__main__':
    pass

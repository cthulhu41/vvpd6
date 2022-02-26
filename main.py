"""Медведев Павел Сергеевич Лаборатнорная работа №4 по ВВПД Вариант 11 КИ21-17/1Б"""


def is_full_connected(v, r):
    """
    Функция определяет полносвязность
    """
    if r == (v * (v - 1)):
        return True
    else:
        return False


def connection_type(r, links):
    """
    Функция определеяет тип связи
    """
    dct = {}
    for i in links:
        if i[0] in dct:
            dct[i[0]].add(i[1])
        else:
            dct[i[0]] = {i[1]}
        if i[1] in dct:
            dct[i[1]].add(i[0])
        else:
            dct[i[1]] = {i[0]}
    checker = 0
    for i in dct:
        if len(dct[i]) == 1:
            continue
        elif len(dct[i]) == r:
            checker = 1
        else:
            break
    if checker:
        return 3
    count = 0
    for i in dct:
        if len(dct[i]) == 1:
            count += 1
        elif len(dct[i]) == 2:
            continue
        else:
            return -1
    else:
        if count == 0:
            return 2
        elif count == 2:
            return 1
        else:
            return -1


if __name__ == '__main__':
    print('1 - Шина\n2 - Кольцо\n3 - Звезда\n-1 - Не относится ни к одному из данных типов')

    first = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2),
             (4, 3)]
    second = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)]
    third = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    fourth = [(1, 2), (1, 3), (1, 4), (1, 5)]
    fifth = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3)]

    # Сеть является полносвязной
    print(f'\nПолносвязная - {is_full_connected(4, 12)}, тип - "{connection_type(12, first)}"')

    # Сеть является неполносвязной, кольцо
    print(f'\nПолносвязная - {is_full_connected(5, 5)}, тип - "{connection_type(5, second)}"')

    # Сеть является неполносвязной, шина
    print(f'\nПолносвязная - {is_full_connected(6, 5)}, тип - "{connection_type(5, third)}"')

    # Сеть является неполносвязной, звезда
    print(f'\nПолносвязная - {is_full_connected(5, 4)}, тип - "{connection_type(4, fourth)}"')

    # Сеть является неполносвязной и не относится ни к одному из типов
    print(f'\nПолносвязная - {is_full_connected(4, 5)}, тип - "{connection_type(5, fifth)}"')

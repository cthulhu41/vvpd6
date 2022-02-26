"""Медведев Павел Сергеевич Лаборатнорная работа №4 по ВВПД Вариант 11 КИ21-17/1Б"""


def is_full_connected(v, r):
    if r == (v * (v - 1)):
        return True
    else:
        return False


def connection_type(r, links):
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

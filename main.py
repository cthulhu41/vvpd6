"""Медведев Павел Сергеевич Лаборатнорная работа №4 по ВВПД Вариант 11 КИ21-17/1Б"""


def is_full_connected(v, r):
    if r == (v * (v - 1)):
        return True
    else:
        return False

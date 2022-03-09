# Алгоритм задачи "Про топологию сетей"
## Постоновка задачи
Сетевая топология – это, по сути, граф, вершинами которого являются компьютеры и маршрутизаторы, а рёбрами – связи между вершинами. Сеть, в которой каждый компьютер непосредственно связан со всеми остальными, называется полносвязной. Остальные сети, соответственно, являются неполносвязными и разделены на несколько типов, три их которых: шина, кольцо и звезда (рисунок 11.1). На основании имеющихся данных о количестве вершин, рёбер и связях между вершинами можно точно определить, какая топология сети перед нами.

![ ](https://downloader.disk.yandex.ru/preview/d3a30cc6eaf60f6c855b800e3e579d050bceefbe1d0986a7640cad03fddbd996/62288db0/2kkeAbtCPWaZMO23NzJGrhf6XQgVANSylIaVcqtL-uO5CnvvvN5TICYqy7-S-yEVyqvvEXGCyO-6Pk8_M-sphQ%3D%3D?uid=0&filename=%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F%20%D1%81%D0%B5%D1%82%D0%B5%D0%B9.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
### Необходимо написать две функции:
- первая будет определять, является ли заданная сеть полносвязной;
- вторая будет определять, к какому типу неполносвязных сетей относится заданная сеть.
## Входные данные
На вход каждой функции подается сначала два целых положительных числа V и R – число вершин и рёбер в графе соответственно (𝑉 > 4, 𝑅 > 3), а затем массив P из кортежей целых чисел (i, j), где пара i, j – наличие связи между вершинами под номерами i и j (𝑉 > 𝑖 > 0, 𝑉 > 𝑗 > 0).
# Реализация алгоритма
### [Подробное описание работы см. в документации main.py](https://github.com/cthulhu41/vvpd6/blob/main/main.py)
## 1 этап
Реализована функция, которая проверяет является ли сеть полносвзяной.
```
def is_full_connected(v: int, r: int):
  if r == (v * (v - 1)):
    return True
  else:
    return False
```
## 2 этап
Реализована функция, которая определяет к какому типу неполносвязных сетей относится данная.
```
def connection_type(r: int, links: list):
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

```

# Полезные ресурсы
[Python для начинающих](https://www.cyberforum.ru/python-beginners/)

[StackOverflow](https://ru.stackoverflow.com/)

[Хабр](https://habr.com/ru/all/)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def get_random_array(array_len: int) -> list[int]:
    return [randint(0, 9) for _ in range(array_len)]

n = int(input('Введите размер массива: '))
list_1 = get_random_array(array_len=n)
list_2 = []
max = int(input('Введите максимум диапазона: '))
min = int(input('Введите минимум диапазона: '))

# print(list_1)
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')
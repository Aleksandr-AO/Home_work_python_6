# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1, d, n = int(input('Первый элемент:\n')), int(input('Разность\n')), int(input('Количество элементов:\n'))
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
mas=[random.randint(-10, 10) for i in range(random.randint(10,20))]
print(mas)
maxi=int(input("Enter MAX= "))
mini=int(input("Enter MIN= "))
masi=[]
if maxi>=mini:
   for i in range(len(mas)):
      if maxi>=mas[i] and mini<=mas[i]:
          masi.append(i)
   print("Количество:",len(masi))
   print("Индексы:",masi)


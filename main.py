# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

list_el = []
def func():

    f_num = int(input('Введите первый элемент:'))
    s_num = int(input("Введите шаг элементов:"))
    t_num = int(input("Введите количество элементов:"))
    for i in range(t_num):
        if i == 0:
            list_el.append(f_num)
        else:
            f_num += s_num
            list_el.append(f_num)

def list_num():
    for i in list_el:
        print(i)
func()
list_num()


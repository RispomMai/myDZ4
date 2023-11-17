"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def wait_correct_input(data,data_true):
    while data != data_true:
        print("Не верно")
        data = input('Попробуйте еще раз:')

year = input('Ввведите год рождения А.С.Пушкина:')
wait_correct_input(year,'1799')

day = input('Ввведите день рождения Пушкина?')
wait_correct_input(day,'6')

print('Верно')

print('Второй вариант')
def wait_correct_input(data,data_true,stroka):
    while data != data_true:
        print("Не верно")
        print('Введите ',stroka,end='')
        data = input()

year = input('Ввведите год рождения А.С.Пушкина :')
wait_correct_input(year,'1799','год рождения А.С.Пушкина : ')

day = input('Ввведите день рождения Пушкина :')
wait_correct_input(day,'6','день рождения Пушкина : ')

print('Верно')
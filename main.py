from random import randint
from functools import reduce
import zip
# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = "абы абв лфв абй бвф жло кабв"
print(" ".join(i for i in text.split() if not "абв" in i))

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


def pick(name, hand, candys):
    while True:
        if "bot" in name:
            if candys % (hand+1) != 0:
                return candys % (hand+1)
            else:
                return randint(1, hand)
        else:
            i = int(input(f"Какое кол-во конфет вы возьмете {name}? "))
            if 0 < i <= hand:
                return i
            else:
                print(f"Вы можете взять от 0 до {hand}")


candys = int(input("Введите кол-во конфет: "))
max_hand = int(
    input("Введите максимальное кол-во конфет которое можно взять: "))
print("Для игры с ботом укажите имя, частью которого является \"bot\"\nНапример: bot, robot...")
c_playrs = [input(f"Введите имя {i} игрока: ") for i in range(1, 3)]
turn = randint(0, 1)

while candys > 0:
    print(f"На столе осталось: {candys}")
    print(f"Ходит {c_playrs[turn]}")
    candys -= pick(c_playrs[turn], max_hand, candys)
    turn = ~turn
print(f"Победил {c_playrs[~turn]}")

# Создайте программу для игры в ""Крестики-нолики"".


def draw(fld):
    for i in range(1, len(fld)):
        print(f"{fld[i]} ", end="")
        if i % 3 == 0:
            print()


def win(fld):
    win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in win_list:
        if fld[i[0]] == fld[i[1]] == fld[i[2]]:
            return False
    return True


def turn(id, fld):
    while True:
        x = int(input("Укажите номер ячейки: "))
        if x < 1 or x > 9 or not fld[x].isdigit():
            print("Недопустимый ход")
        elif id > 0:
            fld[x] = "x"
            return
        else:
            fld[x] = "o"
            return


field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
t_playrs = [input(f"Введите имя {i} игрока: ") for i in range(1, 3)]
id_plr = randint(0, 1)
while win(field):
    draw(field)
    print(f"Ход игрока {t_playrs[id_plr]}")
    turn(id_plr, field)
    id_plr = ~id_plr
print(f"Победил игрок {t_playrs[~id_plr]}")

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
text_to_zip = "ааабаббсабб"
smth_text = zip.zip(text_to_zip)
print(smth_text)
print(zip.restored(smth_text))

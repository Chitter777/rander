import random
import math
import time
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
import os

os.system('title Rander')
os.system('cls')

startRand = None
endRand = None
__while = None
cmd = None
num = None
fors = 0
err = 0

n = '[RANDER]'
i = f'{n} | [INFO] | '
w = f'{n} | [WARN] | '
g = f'{n} | [GEN] | '
inp = f'{n} | [AWAIT INPUT] |> '


while fors != None:
    cmd = input(inp)
    if cmd == "about":
        print(f'{i}RANDER - это небольшая программа по рандомизации, ака "Лохотрон" :3')
        print()
        print(f"{i}Проект был залит на GitHub: https://github.com/Chitter777/rander. \n Мой дискорд: Chitter777#0070")
    elif cmd.startswith("help"):
        if cmd.endswith(" about"):
            print(f"{i}" + Fore.YELLOW + "about" + Style.RESET_ALL + " - о программе"),
        elif cmd.endswith(" cls"):
            print(f"{i}" + Fore.YELLOW + "cls" + Style.RESET_ALL + " - очистить экран программы"),
        elif cmd.endswith(" exit"):
            print(f"{i}" + Fore.YELLOW + "exit" + Style.RESET_ALL + " - закрытие программы" + Style.RESET_ALL),
        elif cmd.endswith(" start"):
            print(f"{i}" + Fore.YELLOW + "start" + Style.RESET_ALL + " - начать процесс генерации" + Style.RESET_ALL),
        else:
            print(f"{i}Все команды: " + Fore.YELLOW + "about" + Style.RESET_ALL + ", " + Fore.YELLOW + "cls" + Style.RESET_ALL + ", " + Fore.YELLOW + "exit" + Style.RESET_ALL + ", " + Fore.YELLOW + "help" + Style.RESET_ALL + ", " + Fore.YELLOW + "start" + Style.RESET_ALL),
    elif cmd == "start":
        time.sleep(0.2)
        print(f"{inp}Для того, чтобы задать диапазон генерации, нужно сначала указать наименьшее нужное число, потом - наибольшее нужное. И наконец, число-цель.")
        time.sleep(0.1)
        print(f'{inp}Для того, чтобы выйти из программы, укажите ' + Back.YELLOW + "0" +Style.RESET_ALL + ' в каждый аргумент')
        print()
        time.sleep(2)
        startRand = int(input(f"{inp}Введите число начала генерации: "))
        endRand = int(input(f"{inp}Введите число конца генерации: "))
        __while = int(input(f"{inp}Введите число-цель генерации: "))
        if startRand == 0 and endRand == 0 and __while == 0:
            print()
            print(Back.YELLOW + f"{i}Выход из программы..." + Style.RESET_ALL)
            time.sleep(3)
            break
        print()
        while num != __while:
            if startRand == endRand or __while < startRand or __while > endRand:
                err = 1
                break
            elif startRand < 0 and endRand < 0:
                if abs(startRand) < abs(endRand):
                    err = 2
                    break
            else:
                num = random.randint(startRand, endRand)
                fors += 1
                print(f"{g}Генерация: {num}")
                #time.sleep(0.03)
            err = 0
        if err == 0:
            print("____________________________")
            print()

        allNum = abs(endRand - startRand)
        if allNum == 0:
            print(Back.RED + f"{w}Диапазон равен 0." + Style.RESET_ALL)
            time.sleep(1)
        elif err == 1:
            time.sleep(1)
            print(Back.RED + f"{w}Число вне указанного диапазона." + Style.RESET_ALL)
            print()
            time.sleep(1)
        elif err == 2:
            time.sleep(1)
            print(Back.RED + f"{w}Диапазон указан неправильно." + Style.RESET_ALL)
            print()
            time.sleep(1)
        else:
            print(Fore.GREEN + f"{i}Ваше число: {__while}" + Style.RESET_ALL)
            print(Fore.GREEN + f"{i}Всего доступных чисел для генерации: {allNum}" + Style.RESET_ALL)
            print(Fore.GREEN + f"{i}Количество генераций: {fors}" + Style.RESET_ALL)
            fors = 0
            num = None
            __while = None
            time.sleep(2)
            print()

    elif cmd == "exit":
        print(Back.YELLOW + f"{i}Выход из программы..." + Style.RESET_ALL)
        time.sleep(3)
        break
    elif cmd == "cls":
        os.system('cls')
    else:
        print(Back.YELLOW + f"{w}Команда введена неверно. Введите help для справки." + Style.RESET_ALL)
        time.sleep(1)

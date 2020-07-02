import random
import time
import pygame
import datetime
import tkinter

from tkinter import *
#################
LOL = True
spisok = [0,"test.txt","random.txt","text.txt"]
nolik = 0
################
def add():
    print("")
def delete(b):
    spisok.pop(b)   
    print("список был успешно показан.")
def view(a):
    print(a)
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb
#################
while True:
    print("1.Просмотреть файловую систему")
    print("2.Добать файл в файловую систему")
    print("3.Удалить файл с файловой системы")
    print("4.Посмотреть содержимое файла")
    print("5.timer")
    print("6.date")
    answer = int(input("- "))
    if answer == 1:
        print(view(spisok))
    if answer == 2:
        file_name = input("file name - ")
        print(file_name," вы уверены?")
        vot = int(input("1 - Да. 2 - Нет. >>> "))
        if vot == 1:
            with open(file_name, "w") as file:
                file.write("test")
            print("файл был успешно добавлен.")
            spisok.append(file_name)
        if vot == 2:
            file_name = input("file name - ")
        print("")
    if answer == 3:
        print(spisok)
        otvet = int(input("Под каким номером вы хотите удалить файл? >>> "))
        delete(otvet)
        print("список был успешно удален.")
        print(spisok)       
    if answer == 4:
        vi = int(input("Под каким номером файл, который вы хотите посмотреть? >>> "))
        name_file = spisok[vi]
        with open(name_file, 'r') as f:
            data = f.read()         
        fo = int(input("Хотите в него что-то добавить??? 1.Да / 2.Нет >>> "))
        if fo == 1:
            with open('data.txt', 'w') as f:
                auf = input(' > > > ')
                f.write(auf)
            print("Данные были успешно добавлены.")
    if answer == 5:
        print("На какой минуте остановиться?")
        vvv_min = int(input(" "))
        vvv_proverka = True
        sec = 0
        minute = 0
        while vvv_proverka == True:
            if minute < vvv_min:
                if sec <= 60:
                    sec = sec + 1
                    print(sec,"sec","",minute,"minute")
                    time.sleep(1)
                if sec >= 60:
                    sec = 0
                    minute = minute + 1
                    print("прошла минута!!!")
            if minute == vvv_min:
                vvv_proverka = False
    if answer == 6:
        vvv_date =202000000#datetime.datetime.now()
        print(vvv_date[0],vvv_date[1],vvv_date[2],vvv_date[3])  
                
#    else:
#       print("Такого выбора нет, попробуйте еще раз.")
#       print("")

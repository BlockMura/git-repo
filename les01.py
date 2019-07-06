# coding: utf-8

import os
import psutil        #этот модуль сторонний...для установки используем pip install psutil
import sys 
import shutil


def duplicate_file(dubl):
    if os.path.isfile(dubl):
        newfile = dubl + '.dupl' 
        shutil.copy(dubl, newfile)   #копирование
        if os.path.exists(newfile):
            print("файл", newfile, "был создан")
            return True
        else:
            print("Ошибка копирования")
            return False
            
            
def sys_infor():
    print("Вот что я знаю о системе:")
    print("количество процессоров:", os.cpu_count())
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Текущая дерриктория:", os.getcwd())
    print("Текущий пользователь:", os.getlogin())


def del_duplicate(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0

    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                doubl_count += 1
                print("файл", fullname, "удален")
    return doubl_count

    
# комментарий

print("Крутая программа")
print("Привет програмист")
name = input("Как вас зовут:")
print(name,", Добро пожаловать в мир Python")

# PEP-8

answer = ''
while answer != 'q':
    answer = input("Давайте поработаем? (Y/N/q)")
    if answer == 'Y':  
        print("Да хозяин")
        print(" [1] - выведу список файлов")
        print(" [2] - выведу информацию о системе")
        print(" [3] - вывести список процессов")
        print(" [4] - дублирование файлов текущей дирректории")
        print(" [5] - выберите файл для дублирования")
        print(" [6] - удаление дублированных файлов")
        do = int(input("укажите номер действия:"))
        
        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_infor()
            
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("Дублирование файлов в текужей дирректории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
                 
        elif do == 5:
            print("Дублирование файла")
            dubl = input('укажите дублируемый файл:')
            duplicate_file(dubl) 
            
        elif do == 6:
            print("=Удаление дублируемых файлов=")
            dirname = input("Введите имя директории:")
            count = del_duplicate(dirname)
            print("--Удалено файлов", count)
        else:
            pass
# type, dir, help, cpu_affinity, os.getpid, psutil.Process, users
    elif answer == 'N':
        print("До свидание")
    else:
        print("Неизвестный ответ")

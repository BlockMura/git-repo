# coding: utf-8

import os
#import psutil        #этот модуль сторонний...для установки используем pip install psutil
import sys 
import shutil
import random


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

def duble_file(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1            
                
def sys_infor():
    print("Вот что я знаю о системе:")
    print("количество процессоров:", os.cpu_count())
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Текущая директория:", os.getcwd())
    print("Текущий пользователь:", os.getlogin())

def del_random_file(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print('файл', fullname, 'случайно удален')


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
    
def main():    
    print("Крутая программа")
    print("Привет программист")
    name = input("Как тебя зовут:")
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
            print(" [7] - удаление случайного файла из папки")
            do = int(input("укажите номер действия:"))
            
            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_infor()
                
            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                print("Дублирование файлов в текужей дирректории")
                duble_file('.')
                     
            elif do == 5:
                print("Дублирование файла")
                dubl = input('укажите дублируемый файл:')
                duplicate_file(dubl) 
                
            elif do == 6:
                print("=Удаление дублируемых файлов=")
                dirname = input("Введите имя директории:")
                count = del_duplicate(dirname)
                print("--Удалено файлов", count)
            elif do == 7:
                print("Удаление случайного файла из указанной директории")
                dirname = input("Введите имя директории:")
                del_random_file(dirname)
                
            else:
                pass
    # type, dir, help, cpu_affinity, os.getpid, psutil.Process, users
        elif answer == 'N':
            print("До свидание")
        else:
            print("Неизвестный ответ")

if __name__ == "__main__":
    main()
            
            
            
            
def del_random_file(dirname):
    file_list = os.listdir(dirname)
    for i in file_list:
        fullname = os.path.join(dirname, random(i))
        os.remove(fullname)
        
        
print("Удаление случайного файла из указанной директории")
dirname = input("Введите имя директории:")
del_random_file(dirname)
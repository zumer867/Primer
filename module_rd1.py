#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Student3
#
# Created:     25.12.2016
# Copyright:   (c) Student3 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    list_k = []
    #list_k = ['Команда1', 'Команда2'. 'Команда3']
    i = 10
    a = '-'


    while  i == 10:
        a = input("Введите команду >")
        if a == "q":
            i = 1
            print('Ok')
        if a == "Команда1":
            print("Выполняю Команду1 \n")
            pass
        if a == "Команда2":
            print("Выполняю Команду2 \n")
            pass
        if a == "Команда3":
            print("Выполняю Команду3 \n")
            pass


        pass

if __name__ == '__main__':
    main()







com = 0
book = {}
while not com == 5:   
    f = open('cash', 'a+')
    print("Введите номер соответсвующей функции:\
    	\n1 - добавить контакт\
    	\n2 - удалить контакт\
    	\n3 - найти контакт\
    	\n4 - показать все контакты\
    	\n5 - выход из программы"
    	 )
    com = int(input())

    if com in range (1, 6):
        if com == 1:
            new = str(input("Введите новый контакт: "))
            new = new.split(' ', 1)
            name = new[0]
            num = new[1]  
            book[name] = num
            book.update
            f.write('{0} : '.format(name))
            f.write('{0} \n'.format(num))
            print("Контакт {0} добавлен!".format(name))
        if com == 4:
           f.seek(0,0)
           q =  f.readlines()
           print(q)
           '''print("Найдено контактов:", len(book))
            for name, num in book.items():
                print("{0:1}:{1:1}".format(name, num))'''

        if com == 2:
            de1 = str(input("Какой контакт хотите удалить? "))
            if de1 in book:
                del book[de1]
                print("Контакт {0} был успешно удален".format(de1))
            else:
                print("Такой контакт не существует")

        if com == 3:
            #ищет только одно совпадение(другие исключает update) и выводит номер
            schg = str(input("Какой контакт хотите найти? "))
            if schg in book:
                print("Контакт с именем {0} найден, номер:{1}".format(schg, book[schg]))
            else:
                print("Контактов с таким именем не обнаружено")        
        if com == 5:
            f.close()
            print("Goodbye!")   
    else:
        print("Введено неправильное значение")


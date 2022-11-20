import random
listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]
def delete(list,del_range):
    print(f'Полный список желающих поехать на поход:\n{list}')
    for i in range(del_range):
        name=list.pop(random.randrange(len(list)))
        print(f'Со списка людей удалили:{name}')
    print(f'Список тех кто поедут на поход:\n{list}')
delete(listNames,4)



#Task2
def human():
    list=[]
    a=int(input("Случайная длина для вашего списка людей:"))
    for i in range(a):
        i+=1
        b=input(f"Введите имя для {i} человека:")
        list.append(b)
    print(f'Список из {a} людей')
    print(f"Случайный список из {a} людей:",list)
human()



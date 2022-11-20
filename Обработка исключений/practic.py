#Task2
def num():
    try:
        a = int(input("Введите:"))
        print(f'{a ** 2} {a ** 3}')
    except ValueError:
        print("ошибка")
num()
#Task3
def findResult(n1, n2, n3):
    result = 0
    try:
        result = n1/n2/n3
    except ZeroDivisionError:
        result = 'Вы пытаетесь делить на ноль'
    except TypeError:
        result = 'Вы ввели строку!'
    except BaseException as be:
        result  = f'Неизвестная ошибка {be}'
    finally:
        return result
print(findResult())
#Task4
def nv(x,y,z=4):
    try:
        print(f"Деления чисел:{x}:{y}:{z}={x / y / z}")
    except ValueError:
        print("Вы ввели строку")
    except ZeroDivisionError:
        print("Вы пытаетесь делить на ноль")
    except BaseException as fg:
        print("Неизвестная ошибка")

nv(200,0)
nv(105,48,5)
nv("djfkl","dlfkjg")
#Task5
def number(n1,n2,n3):
    try:
        for i in range(n1, n2, n3):
            print(i)
    except TypeError:
        print("Ошибка вы ввели строку")
    except ZeroDivisionError:
        print("Нол")
    except BaseException as df:
        print("Неизвестная ошибка")
number(1,90,0)
#Task6
def number(mylist):
    try:
        for i in mylist:
            if i % 2 == 0:
                list1.append(i)
            else:
                list.append(i)
    except TypeError:
        print("Вы ввели строку")
    except BaseException as fdg:
        print("Неизвестная ошибка")
    finally:
        print("\U0001f61b")
myList = [213, 45, 546, 67, 234, 654, 33, 31,
46,100,105,106,10007,120]

list1=[]
list=[]
number(myList)
print("Нечетные числа:",list)
print("Четные числа:",list1)


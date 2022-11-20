#Task1
def nuM():
    try:
        number = int(input("Введите число:"))
        a = str(number)
        print(a[::-1])
    except:
        print("Вы ввели строку")
nuM()
#Task2
def number(*nums):
    sum = 0
    try:
        for n in nums:
            sum += n
        print("Average number: ", sum / len(nums))
    except TypeError:
        print("Вы ввели строку")
    except BaseException :
        print(f"Неизвестный ошибка")
    finally:
        print("Удачи")
number("f,d")
number(5,7,0)
#Task3
def unikalnyi_chislo(number:int):
    try:
        a = set(number)
        b = list(a)
        print(b)

    except IndexError:
        print("Ошибка")
    except ValueError:
        print("Вы не ввели числовый значения")
unikalnyi_chislo([])
#Task4
def numbers(a,b,c):
    try:
        x = 0
        if a > 0:
            x += 1
        if b > 0:
            x += 1
        if c > 0:
            x += 1
        print("Количество положительных чисел: ", x)
        y = 0
        if a < 0:
            y += 1
        if b < 0:
            y += 1
        if c < 0:
            y += 1
        print("Количество отрицательных чисел: ", y)
    except TypeError:
        print("Ввели строку!!!")
numbers("f","d","c","d")
#Task5
def nuMbers():
    try:
        a = int(input("Введите:"))
        b = int(a / 10)
        c = a % 10
        print("Sum:", b + c)
        print("proizvedenie:", b * c)
    except ValueError:
        print("Вы ввели строку")
    except BaseException:
        print("Неизвесная ошибка")
    except ZeroDivisionError:
        print("Вы пытаетесь делить на ноль")
nuMbers()
#Task6
def transport():
    try:
        a = int(input("Введите веса посылки:"))
        if a > 0 and a <= 2:
            print("Стоимость товар:", a * 3)
        elif a >= 3 and a <= 5:
            print("Стоимость товар:", a * 5.5)
        elif a >= 6 and a <= 10:
            print("Стоимость товар:", a * 7)
        elif a <= 50:
            print("Cтоимость товар:", a * 10)
        else:
            print("Посылка не может быть отправлена!!!")
    except ValueError:
        print("Вы ввели строку")
transport()
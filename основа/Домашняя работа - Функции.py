#Task1
def nuM():
    number=int(input("Введите число:"))
    a=str(number)
    print(a[::-1])
nuM()
#Task2
def number(*nums):
    sum = 0
    for n in nums:
        sum += n
    print("Average  number: ", sum/len(nums))
number(3, 5)
number(4, 5, 6, 7)
number(1, 2, 3, 5, 6)
number(1, 2, 3, 5, 6,12,15)
#Task3
def unikalnyi_chislo(number):
    a=set(number)
    b=list(a)
    print(b)
unikalnyi_chislo([1,11,2,1,2,3,4,5,5,4,1,11,12,9,9,8,7,6,6,5])
#Task4
def numbers(a,b,c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c> 0:
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
numbers(-1,2,-2)
#Task5
def nuMbers():
    a=int(input("Введите:"))
    b=int(a/10)
    c=a%10
    print("Sum:",b+c)
    print("proizvedenie:",b*c)
nuMbers()
#Task6
def transport():
    a=int(input("Введите веса посылки:"))
    if a>0 and a<=2:
        print("Стоимость товар:",a*3)
    elif a>=3 and a<=5:
        print("Стоимость товар:",a*5.5)
    elif a>=6 and a<=10:
        print("Стоимость товар:",a*7)
    elif a<=50:
        print("Cтоимость товар:",a*10)
    else:
        print("Посылка не может быть отправлена!!!")
transport()







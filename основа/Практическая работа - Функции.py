#Task1
def name(a=input("Имя:")):
    print(f"Привет {a}, добро пожаловать в нашу программу!")
name()
#Task2
def nuM(b=int(input("Введите число:"))):
    print(f"квадрат:{b**2 }  куб:{b**3}")
nuM()
#Task3
def calcAvg(num1,num2,num3):
    print(f"{(num1+num2+num3)/3}")
num1=int(input("Введите:"))
num2 = int(input("Введите:"))
num3 = int(input("Введите:"))
calcAvg(num1,num2,num3)
#Task4
def nv(x,y,z=4):
    print(f"Деления чисел:{x}:{y}:{z}={x/y/z}")
nv(200,40)
nv(105,48,5)

#Task5
def number(n1,n2,n3):
    for i in range(n1,n2,n3):
        print(i)
number(1,90,5)

#Task6
def number(mylist):
    for i in mylist:
        if i%2==0:
            list1.append(i)
        else:
            list.append(i)
myList = [213, 45, 546, 67, 234, 654, 33, 31, 46,100,105,106,10007,120]
list1=[]
list=[]
number(myList)
print("Нечетные числа:",list)
print("Четные числа:",list1)




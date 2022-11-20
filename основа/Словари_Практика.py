#Task1
elem=int(input("Количество элементов:"))
key=input("Ключ:")
znach=input("Значение:")
keys1=input("Ключ:")
znach2=int(input("Значение:"))
key2=input("Ключ:")
znach3=float(input("Значение:"))
name={key:znach,keys1:znach2,key2:znach3}
print(name)

#Task2
numbers={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight"}
# number=numbers.pop(1)
print(numbers)
# number1=numbers.pop(3)
print(numbers)
del numbers[8]
print(numbers)
numbers.clear()
print(numbers)


#Task3
num={1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
num_1=num.values()
for i in num_1:
    print(i)
print("*"*25)
num_2=num.keys()
for j in num_2:
    print(j)
print("*" * 25)
#Task4
dictNum={}
for i in range(1,8):
    dictNum[i]=i**2
print(dictNum)
print("*" * 25)

#Task5
d = {"Один" : "Питон", "Два" : "C++", "Три" : "Java", "Четыре" : "C#"}
#Task1
l_progamming=["Programming", "Java", "Python", "JavaScript", "C#"]
m="-".join(l_progamming)
print(m)

#Task3
city="Москва, Лондон, Бишкек, Куала Лумпур, Сингапур, Токио".split()
print(sorted(city))

#Task4
numbers=int(input("Введите число:"))
print("Узнайте корень данного числа:",numbers**0.5)
print("Возведите в 3 степень:",numbers**3)
print("Узнайте десятичный логарифм данного числа",10**numbers)
f=1
while numbers>1:
    f*=numbers
    numbers-=1
print("Узнайте факториал этого числа:",f)

#Task5
dic={}
l=int(input("Введите длину словаря:"))
for i in range(0,l):
  dic[input("Введите ключ:")] = (input("Введите значение:"))
print(dic)



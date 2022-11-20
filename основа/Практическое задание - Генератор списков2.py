#Task1
name=input("Введите ваше имя: ")
names=[name for i in range(10)]
print(names)

#Task2
numbers=[i/3 for i in [18,43,9,65,12,65,24,6]]
print(numbers)

#Task3
numberS=[i for i in [18,43,9,65,12,65,24,6] if i%3==0]
print(numberS)

#Task4
city=input("Принятые от пользователя города:").split()
cities=["Совпадает" if i=='Tokyo' else "Не совпадает" for i in city]
print(cities)

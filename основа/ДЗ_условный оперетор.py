#1
numbers=int(input("Введите число: "))
if numbers>2 and numbers<9:
    print("Число больше 2 и меньше 9")
else:
   print("Неизвестное число")
print("-"*30)
#b
number=int(input("Введите число: "))
num="Число больше 2 и меньше 9" if number>2 and number<9  else "Неизвестное число"
print(num)

print("-"*30)
#2
weight=float(input("Ввести вес посылки :"))
if weight<=2:
  print(weight*3.5)
elif weight>=3 and weight<=5:
   print(weight*5.5)
elif weight>=6 and weight<=10:
    print(weight*7)
elif weight<=50:
    print(weight*10)
else:
    print("посылка не может быть отправлена")
print("-"*30)
#3
nuMber1=float(input("Ввести число:"))
if nuMber1 % 2==1:
    print("Число нечетный")
else:
    print("Перезапустить программу заново")







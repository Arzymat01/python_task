#1
# i = 1
# user=(input("Введите имя пользователя:"))
# while i<=20:
#     print(user)
#     i+=1


#2
# for i in range(5,135,3):
#    while i%5==0 :
#      print(i)
#      break
#3

number=int(input("Введите число:"))
while(number):
 number = int(input("Введите число:"))
 if number==0:
  print("Выход из вычисления!")
  break
 print("Выход из довабления 10-ти:",number+10)

#4
# k=34
# while k<=67 :
#     k % 2 == 0
#     print(k)
#     k+=1

# str = input("Введите текст: ")
# number = int(input("Ввдетиде число: "))
# for i in str:
#     print(i*number)
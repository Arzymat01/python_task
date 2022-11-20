1
num_1=int(input("Число_1:"))
num_2=int(input("Число_2:"))
if num_1>num_2:
    print("первое число больше")
elif num_1 == num_2:
    print("два числа равны")
else:
    print("второе число больше")
print("-"*30)
2
opeR = int(input("Введите номер операции: 1.Сложение 2.Вычитание 3.Умножение:"))
if opeR==1:
 print("Сложения")
elif opeR == 2:
    print("Вычитания")
elif opeR == 3:
    print("Умножения")
else:
   print( "не определен")
print("-"*30)
3
nuM_1 = int(input("Первое число: "))
nuM_2 = int(input("Второе число: "))
opeR_2 = int(input("Введите номер операции: 1.Сложение 2.Вычитание 3.Умножение:"))
if opeR_2 == 1:
 reS = nuM_2+nuM_1
elif opeR_2 == 2:
    if nuM_1 >= nuM_2:
        reS=nuM_1-nuM_2
    else:
        reS=nuM_2-nuM_1
elif opeR_2 == 3:
    reS=nuM_1*nuM_2
else:
    reS="не определена"
print(reS)
print("-"*30)
#4
number_Ch=int(input("Введите число:"))
if number_Ch%2==0:
    print("Это число является четным значением!")
else:
    print("Это число НЕ является четным значением!")
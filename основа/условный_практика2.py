#1
num_1=int(input("Num_1:"))
num_2=int(input("Num_2:"))
num_3=int(input("Num_3:"))
if num_1>num_2:
    if num_1>num_3:
        print(f"Максимальное число:{num_1}")
    else:
        print(f"Максимальное число:{num_3}")
else:
    if num_2>num_3:
        print(f"Максимальное число:{num_2}")
    else:
        print(f"Максимальное число:{num_3}")

#2
city_1=input("Город1:")
city_2=input("Город2:").lower()
if city_1[-1]==city_2[0]:
    print("Good")
elif city_1[-1]=="ь":
        if city_1[-2]== city_2[0]:
            print("Good")
        else:
            print("Bad")
else:
    print("Bad")

#3
month_num = int(input('Month num: '))

match month_num:
    case 1:
        print('Январь - 31 день')
    case 2:
        print(' Февраль - 28 дней')
    case 2:
        print(' Март - 31 день')
    case 3:
         print('  Апрель - 30 дней')
    case 4:
        print(' Май - 31 день')
    case 5:
        print(' Июнь - 30 дней')
    case 6:
        print('Июль - 31 день')
    case 7:
        print('Август - 31 день')
    case 8:
        print('Сентябрь - 30 дней')
    case 9:
        print('Октябрь - 31 день')
    case 10:
        print('Ноябрь - 30 дней')
    case 11:
        print(' Декабрь - 31 день')
    case _ :
         print('error')
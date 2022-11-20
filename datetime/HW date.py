from datetime import*
#Task1
custom_date=input("Введите дату и время:")
print(datetime.strptime(custom_date,"%d-%m/%Y-(%H:%M:%S)"))
#Task2
a = datetime(2020, 3, 22,12,45)
print(a.strftime("%d-%B-%A-%e-%I:%M"))


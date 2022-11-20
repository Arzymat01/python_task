from datetime import*
#Task1
day=input(f"Введите день:")
month=input(f"Введите месяц:")
year=input(f"Введите год:")
result=day+ '-' + month+ '-' +year
resultTime=datetime.strptime(result,'%d-%m-%Y')
print(resultTime)
print(f'{resultTime.day}.{resultTime.month}.{resultTime.year}')
#Task2
data=timedelta(weeks=1,hours=2)
now=datetime.now()
data1=now+data
print(data1)
#Task3
data_1=timedelta(days=10)
now_1=datetime.now()
data_2=now_1-data_1
print(data_2)

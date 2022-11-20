import calendar
import pytz
from datetime import *
#Task1
month=int(input("Введите месяц:"))
year=int (input("Введите год:"))
c=calendar.TextCalendar(calendar.TUESDAY)
str=c.formatmonth(year,month)
print(str)
#Task2
month=int(input("Введите месяц:"))
year=int(input("Введите год:"))
for month in range(1,13):
    cln=calendar.monthcalendar(year,month)
    list1=cln[0]
    list2=cln[1]
    if list1[calendar.MONDAY]!=0:
        auditay=list1[calendar.TUESDAY]
    else:
        auditay=list2[calendar.TUESDAY]
    print("%10s %2d"%(calendar.month_name[month],auditay))
#Task3
m=int(input("Введите месяц:"))
y=int (input("Введите год:"))
ht=calendar.HTMLCalendar(calendar.TUESDAY)
str=ht.formatmonth(y,m)
print(str)
#Task4
year=int(input("Введите год:"))
moth=int(input("Введите месяц:"))
day=int(input("Введите ден:"))
hour=int(input("Введите часы:"))
minutes=int(input("Введите год:"))
utc_now = pytz.utc.localize(datetime(year, moth, day, hour, minutes))
dt_france= utc_now.astimezone(pytz.timezone('Europe/Paris'))
dt_Japan= utc_now.astimezone(pytz.timezone('Asia/Tokyo'))
dt_Australia= utc_now.astimezone(pytz.timezone('Australia/Canberra'))
dt_South_Africa= utc_now.astimezone(pytz.timezone('Africa/Johannesburg'))
dt_India= utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
print("Время Франция:",dt_france)
print("Время Япония:",dt_Japan)
print("Время Индия:",dt_India)
print("Время Южная Африка :",dt_South_Africa)
print("Время Австралия:",dt_Australia)
#Task5
dt_france1 = datetime.now(pytz.timezone('Europe/Paris'))
dt_Japan2= datetime.now(pytz.timezone('Asia/Tokyo'))
dt_Australia3 = datetime.now(pytz.timezone('Australia/Canberra'))
dt_South_Africa4 = datetime.now(pytz.timezone('Africa/Johannesburg'))
dt_India5 = datetime.now(pytz.timezone('Asia/Kolkata'))
vrm=int(input("Выбор:"))
if vrm==1:
    print("Сейчас во Франции:",dt_france1)
elif vrm==2:
    print("Сейчас во Япония:",dt_Japan2)
elif vrm==3:
    print("Сейчас во Австралия:",dt_Australia3)
elif vrm==4:
    print("Сейчас во Южная Африка:",dt_South_Africa4)
elif vrm==5:
    print("Сейчас во Индия:",dt_India5)
else:
    print("Ошибка")


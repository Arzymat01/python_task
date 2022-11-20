class Student:
    def __init__(self,name,payment,marks1, marks2,listPr=0):
        self.__name=name
        self.__payment=payment
        self.__marks=dict(marks1=marks2)
        self.__lsitPr=listPr

    def __str__(self):
        return f'Имя человека:{self.name}'

    def __add__(self, other):
        return f'Сумма контрокт двух студента :{self.__payment+other.__payment }'

    def __sub__(self, other):
        return f' Вчитания контракта: {self.__payment-other.__payment}'

    def __mul__(self, other):
        return  self.__payment * other

    def __lt__(self, other):
        return f'Сравнения средних оценок :{self.__marks<other.__marks}'

    def __gt__(self, other):
        return f'Сравнения средних оценок :{self.__marks > other.__marks}'

    def __le__(self, other):
        return f'Сравнения средних оценок :{self.__marks <= other.__marks}'

    def  __ge__(self, other):
        return f'Сравнения средних оценок :{self.__marks >= other.__marks}'

    def __eq__(self, other):
         return f'Сравнения средних оценок :{self.__marks==other}'


std1=Student("Albert",40000,"linner cevir",87, )
std2=Student("Robert",65000,98,"Differential equation")
std3=Student("Alex",78000,89,"History")
print(std1._Student__marks)
print(std1+std2)
print(std3-std2)
print(std3*2)
print(std1<std1)
print(std3>std2)
print(std3<=std2)
print(std3>=std1)
print(std3==105)
print(std3==105)

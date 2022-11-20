from abc import  ABC,abstractmethod
class Car(ABC):
    def __init__(self,model,color,maxSpeed):
        self.model=model
        self.color=color
        self.maxspeed=maxSpeed
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def gass(self):
        pass

class Sedam(Car):
    def __init__(self,model,color,maxSpeed,year,frBakes,dvi):
        super().__init__(model,color,maxSpeed)
        self.year=year
        self.frBakes=frBakes
        self.dvi=dvi
    def brake(self):
        print("Харектристка тормозной системы:"
              "\n"f'Модел машина {self.model}\nГод выпуска:{self.year}'
              f'\nЦвет машина:{self.color}'
              f'\nТормозные механизм колес:{self.frBakes}')
    def gass(self):
        print("Харектристка:"
              f'Модел машина {self.model}\nГод выпуска:{self.year}'
              f'\nЦвет машина:{self.color}'
              f'\nТормозные максисалный скорость:{self.maxspeed}'
              f'\nДвигтаел:{self.dvi}')


class SportCar(Car):
    def __init__(self, model, color, maxSpeed, year, frBakes,):
        super().__init__(model, color, maxSpeed)
        self.year = year
        self.frBakes = frBakes

    def brake(self):
            print("Харектристка тормозной системы:"
                  "\n"f'Модел машина {self.model}\nГод выпуска:{self.year}'
                  f'\nЦвет машина:{self.color}'
                  f'\nТормозные механизм колес:{self.frBakes}')
    def gass(self):
        print("Харектристка:"
              f'Модел машина {self.model}\nГод выпуска:{self.year}'
              f'\nЦвет машина:{self.color}'
              f'\nТормозные максисалный скорость:{self.maxspeed}'
              f'\nДвигтаел:{self.dvi}')





class Family(Car):
    def __init__(self, model, color, maxSpeed, year, frBakes,airbag,belt):
        super().__init__(model, color, maxSpeed)
        self.year = year
        self.frBakes = frBakes
        self.airbag=airbag
        self.belt=belt
    def brake(self):
        print("Харектристка тормозной системы:"
              "\n"f'Модел машина {self.model}\nГод выпуска:{self.year}'
              f'\nЦвет машина:{self.color}'
              f'\nТормозные механизм колес:{self.frBakes}'
              f'\nАирбаг:{self.airbag}'
              f'\nРемень:{self.belt}')

    def gass(self):
        print("Харектристка:"
              f'Модел машина {self.model}\nГод выпуска:{self.year}'
              f'\nЦвет машина:{self.color}'
              f'\nТормозные максисалный скорость:{self.maxspeed}'
              f'\nДвигтаел:{self.dvi}')

car=Family('Merssedes','red',200,2001,19,"yes","yes")
car.brake()

#Task2
class Person(ABC):
    def __init__(self,name,age,salary,profess):
        self.name=name
        self.age=age
        self.sslary=salary
        self.profes=profess
    @abstractmethod
    def calculateMyExpenses(self):
        pass
    @abstractmethod
    def whereToEat(self):
        pass
    @abstractmethod
    def earnMoney(self):
        pass

class Student(Person):
    def __init__(self,name,age,salary,profess,food,clothes,internet,fare,scholarship):
        self.food=food
        self.clothes=clothes
        self.internet=internet
        self.fare=fare
        self.scholarship=scholarship
        super().__init__(name,age,salary,profess)
    def calculateMyExpenses(self):
        expencess=self.food+self.clothes+self.internet+self.fare
        print(f'Имя:{self.name}'
               f'Стмпендия:{self.scholarship}'
              f'Месячные расходы:{expencess}')
    def whereToEat(self):
        print("Еда на кухне")

    def earnMoney(self):
        print(f'Имя:{self.name}\nВозрость:{self.age}'
              f'\nПрофессия:{self.profes}'
              f'\nЗарплата:{self.sslary}')

class Bankworker(Person):
    def __init__(self,name,age,salary,profess,food,clothes,internet,fare,menu):
        self.food=food
        self.clothes=clothes
        self.internet=internet
        self.fare=fare
        self.menu=menu
        super().__init__(name,age,salary,profess)
    def calculateMyExpenses(self):
        expencess=self.food+self.clothes+self.internet+self.fare
        print(f'Имя:{self.name}'
               f'Зарплата:{self.sslary}'
              f'Месячные расходы:{expencess}')
    def whereToEat(self):
        print("Еда на кухне")

    def earnMoney(self):
        print(f'Имя:{self.name}\nВозрость:{self.age}'
              f'\nПрофессия:{self.profes}'
              f'\nЗарплата:{self.sslary}')

class Doctor(Person):
    def __init__(self, name, age, salary, profess, food, clothes, internet, fare):
        self.food = food
        self.clothes = clothes
        self.internet = internet
        self.fare = fare
        super().__init__(name, age, salary, profess)

    def calculateMyExpenses(self):
        expencess = self.food + self.clothes + self.internet + self.fare
        print(f'Имя:{self.name}'
              f'Зарплата:{self.sslary}'
              f'Месячные расходы:{expencess}')

    def whereToEat(self):
        print("Еда на кухне")

    def earnMoney(self):
        print(f'Имя:{self.name}\nВозрость:{self.age}'
              f'\nПрофессия:{self.profes}'
              f'\nЗарплата:{self.sslary}')

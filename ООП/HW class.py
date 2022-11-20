# #Task1
class Aninal:
    def __init__(self,type_animal,sound):
        self.type_naimal=type_animal
        self.sound=sound
    def makeNoice(self):
        print(self.sound)
dog=Aninal('Dog','Гав Гав!')
dog.makeNoice()
cat=Aninal('Cat','Мый Мый!')
cat.makeNoice()
cow=Aninal('Cow','Моу Моу!')
cow.makeNoice()
duck=Aninal('Ducl','Гулу Гулу!')
duck.makeNoice()
#Task2
class Vehicle:
    def __init__(self,brandcar,nameCar,maxSpeed,color):
       self.brand=brandcar
       self.name=nameCar
       self.maxS=maxSpeed
       self.colCar=color
    def info(self):
        print(f'Марка автомобиля:{self.brand}'
              f'\nИмя автомобиль:{self.name}'
              f'\nмаксимальная скорость:{self.maxS}'
              f'\nЦвет:{self.colCar}')
    def cardirec(self):
        if self.maxS<150:
            return "Семейный"
        elif self.maxS<80:
            return "Школьный"
        else:
            return "Спортивный"
def colorchanges(self,color):
    self.colCar=color

car1=Vehicle('Mercedes',"W22",250,"белый")
car2=Vehicle("Audi",'100',120,"красный")
car3=Vehicle("Daewo","Matiz",75,"cиний")
car4=Vehicle("BMW","X5",200,"белый")
car1.colorchanges("черный")
car2.colorchanges("белый")
car3.colorchanges("Красный")
car4.colorchanges("черный")
car1.info()
car2.info()
car3.info()
print(car1.cardirec())
print(car2.cardirec())
print(car3.cardirec())
print(car4.cardirec())

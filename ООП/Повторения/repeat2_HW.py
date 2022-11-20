class ConditionerMixin:
    def __init__(self,model,temperature,mode):
        self.__model=model
        self.__temperature=temperature
        self.__mode=mode
    @property
    def temperature(self):
        return self.__temperature

    def setNewTemperature(self):
        new_Temp=int(input(f'Устоновите новую температура:'))
        self.__temperature=new_Temp

    def modeCond(self):
        if self.__temperature>20:
            self.__mode='Жарко'
        else:
            self.__mode='Холод'
    def off(self):
        self.__temperature=0
        self.__mode='Кондиционер включен'
    def onn(self):
        tempOn=int(input(f'Задайте темрература:'))
        self.__temperature=tempOn
    def display(self):
        print(f'Модел кондиционера:{self.__model} '
              f'\nЗадания {self.__temperature} '
              f'\nРежим работы:{self.__mode}')
class MusicPlayerMixin:
    def playmusic(self,musicname):
        self.__musicname=musicname
        print(f'Проигрываем музыкн{self.musicname}')
class Car(ConditionerMixin,MusicPlayerMixin):
    def __init__(self,modelCar,brandCar,productionYear,musicname,model,temperature,mode):
        self.model=modelCar
        self.brand=brandCar
        self.productionYear=productionYear

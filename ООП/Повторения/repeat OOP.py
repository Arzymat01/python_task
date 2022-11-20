class Conditioner:
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
c1=Conditioner('Samsung',40,'Холод')
c1.setNewTemperature()
print(c1.temperature)
c1.modeCond()
# c1.off()
c1.display()

# class math:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def addition(self):
#         print(self.a+self.b)
#     def multiplication(self):
#         print( self.a*self.b)
#     def division(self):
#         print( self.a/self.b)
#     def subtraction(self):
#         print(self.a - self.b)
# m1=math(5,4)


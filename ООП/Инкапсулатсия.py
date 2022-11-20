class Bank():
    def __init__(self,id,balance):
        self.__id=id
        self.__balance=balance
    def display(self):
        print(f'Банковаский аккаунт #{self.__id}'
              f'\nВаш текуший баланс:{self.__balance}\n')
    def windraw(self,money):
        if money>self.__balance or self.__balance==0:
            print("Недостаточный баланс!")
            return
        self.__balance -=money
        print(f'ВЫ сняли {money} из вашего баланс'
              f'\nи теперь ваш баланс выглядить сд.образом')
        self.display()
    def deposit(self,money):
        if money==0:
            print("Невозможно пополнить нулевым балансом!")

        self.__balance +=money
        print(f'Вы добавили {money} к вашего баланс'
              f'\nи теперь ваш баланс выглядить сд.образом')
        self.display()
b1=Bank("1234568769",5000)
b1.display()
b1.display()
b1.windraw(2000)
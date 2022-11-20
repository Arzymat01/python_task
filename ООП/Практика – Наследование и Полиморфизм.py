class BanAccaount:
    def __init__(self,id, balance):
        self.__id=id
        self.__balance=balance
        self.__limit=10000
        self.__discount=0.1
    def set_id(self,new_id):
        self.__id=new_id

    def get_id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,new_balence):
        self.__balance=new_balence

    @property
    def limit(self):
        return self.__limit
    @limit.setter
    def discount(self,new_limit):
        self.__new=new_limit

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self,new_discount):
        self.__discount=new_discount

    def display(self):
        return (f'Банковский аккаунт #{self.__id}'
                f'\nВаш текуший баланс:{self.__balance}\n')
    def withdraw(self,money):
        if money>self.__balance or self.__balance==0:
            print("Недостфтаточный баланс!")
            return
        if money>self.__limit:
            print('Вы привысили лимит для снятия денег')
            return
        self.__balance-=money
        print(f'Вы сняли {money} из вашего баланса'
              f'\nи теперь ващ баланс выглядить сл.образом:')
        self.display()
    def service(self,purchAmaubt):
        purchAmaubt=purchAmaubt-(purchAmaubt*purchAmaubt)
        self.__balance-=purchAmaubt
    def deposit(self,money):
        if money==0:
            print('Невозможно пополнить нулевым баланса! ')
        if money>self.limit:
            print('Вы превысили лимит для пополнение баланса !')
            return
        self.__balance+=money
        print(f'Вы добавили {money} к вашему баланса '
              f'\nи теперь ваш баланса выглядить сл.образом:')
        self.display()
class Premium_account(BanAccaount):
    def __init__(self,id ,balance):
        self.set_id(id)
        self.balance=balance
        self.limit=50000
        self.discount=0,3
class Vip_account(BanAccaount):
    def __init__(self,id ,balance):
        self.set_id(id)
        self.balance=balance
        self.limit=100000
        self.discount=0,5
ba1 = BanAccaount('12312329213123', 50000)
ba1.deposit()

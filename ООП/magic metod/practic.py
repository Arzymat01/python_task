class BankAccount:
    def __init__(self,id ,balance,ownerName,money):
        self.__id=id
        self.__balance=balance
        self.__overName=ownerName
        self.__money=money

    def __len__(self):
        return len(self.money)

    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return self.__balance*other
        return self.__balance*self.__balance

    def __lt__(self, other):
        if isinstance(other,int):
            return self.__balance<other or isinstance(other,float)
        return self.__balance<self.__balance


    def __gt__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return self.__balance>other
        return self.__balance>self.__balance


    def __ge__(self, other):
        if isinstance(other,int) or isinstance(float,other):
            return self.__balance>=other
        return self.__balance>=other.__balance

    def __le__(self, other):
        if isinstance(int,other) or isinstance(other,float):
            return self.__balance<=other
        return self.__balance<=self.__balance

    def __eq__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return self.__balance==other
        return  self.__balance==other.__balance
    def __add__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return self.__balance+other
        return self.__balance+other.__balance





p1=BankAccount("111899785",97000,'Alex',['euro','som','ruble'])
p2=BankAccount("111899785",89000,'Ivan',['sum','tl','$'])

print(p1*3)
print(p1<p2)
print(p1<480000000)
print(p1==p1)
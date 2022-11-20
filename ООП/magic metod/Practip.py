class Student:
    def __init__(self, name, age, contract, listSubjects):
        self.name = name
        self.contract = contract
        self.age = age
        self.listSubjects = listSubjects

    def __str__(self):
        return (f'Имя человека:{self.name} и вот список его прелметов {self.listSubjects}')

    def __contains__(self, item):
        """
        Проверить присутствие определ предмета среди списка предметов
        """
        return item in self.listSubjects


    def __len__(self):
        """
            Проверит, который взял определенный студент
        """
        return  len(self.listSubjects)

    def __delitem__(self, key):
        """
            Удалить один из предметов
        """
        del self.listSubjects[key]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract + other
        return self.contract + other.contract

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract + other
        return self.contract + other.contract

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract * other
        return self.contract * other.contract

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract * other
        return self.contract * other.contract

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract - other
        return self.contract - other.contract

    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract - other
        return self.contract - other.contract

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract // other
        return self.contract // other.contract

    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            return self.contract // other
        return self.contract // other.contract

    def __call__(self, quantMonth):
        totalContract = (self.contract // 10) * quantMonth
        print(f'Сумма контракта на {quantMonth} вышло: {totalContract}')

s1 = Student('Sergei Vitaliev', 23, 50000,[])
s2 = Student('Oleg Yurevich', 21, 70000)

print(s1 + s2)
print(100000 + s1)

s1(5)
s2(7)









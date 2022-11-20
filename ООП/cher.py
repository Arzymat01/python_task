from abc import  ABC,abstractmethod
class Rondoi(ABC):
    @abstractmethod
    def square(self, a, b):
        return f'Аянты {a*b}'


class Tort(Rondoi):
    ...

class Uch:
    def naaliyt(self):
        print('Наалыбайм')

obj = Esen()
print(obj.square(4,5))


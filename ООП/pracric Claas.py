# #Task1
class dog:
    def __init__(self,name,bread,age,weith):
        self.dogname=name
        self.dofbread=bread
        self.dogage=age
        self.dogweith=weith
    def display_info(self):
        print(f'Кличка: {self.dogname}')
        print(f'\nПорода сабока:{self.dofbread}')
        print(f'\nВозрост собаки:{self.dogage}')
        print(f'\nВес собаки:{self.dogweith}')
    def air(self):
        if self.dogweith<3:
            return True
        else:
            return False
dog1=dog('Borubasar','taigan',3,11)
dog2=dog('Rex','Beagle',1,5)
dog1.display_info()
dog2.display_info()

#Task2
class Alphabet:
    def __init__(self,lang,letters):
        self.language=lang
        self.letts=letters
    def displayletters(self):
        for i in self.letts:
          print(i,end='')
        print()
    def counletts(self):
        return (len(self.letts))
rus=Alphabet('Ru','абгдежзклмн')
eng=Alphabet('En','abcdefhg')
rus.displayletters()
eng.displayletters()
print(rus.counletts())
print(eng.counletts())


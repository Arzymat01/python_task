# #Task1
class Teacher:

    def __init__(self,fio,stj,namepr,numstd):
        self.fio=fio
        self.stj=stj
        self.namepre=namepr
        self.numstd=numstd

    def display(self):
        return self.fio,self.stj,self.namepre,self.numstd

class DrawingTeacher(Teacher):

    def __init__(self,fio,stj,namepr,numstd, figure):
        Teacher.__init__(self,fio,stj,namepr,numstd)
        self.figure=figure

    def findSimilarObject(self):
        if self.figure=='Треугольник':
            return "Пирамида в Египте имеет форму треугольника"
        elif self.figure=='Круг':
            return 'Мир имеет форму круга'
        elif self.figure=='Квадрат':
            return 'Коробка имеет квадратную форму'

    def display(self):
        return self.fio,self.stj,self.namepre,self.numstd, self.findSimilarObject()

class MathTeacher(Teacher):

    def __init__(self,fio,stj,namepr,numstd,*num):
        self.num=num
        Teacher.__init__(self, fio, stj, namepr, numstd)

    def findAvarage(self):
       return sum(self.num)/len(self.num)

    def display(self):
        return self.fio,self.stj,self.namepre,self.numstd, self.findAvarage()

class GeographyTeacher(Teacher):

    def __init__(self,fio,stj,namepr,numstd,capitaL):
        self.capitaL=capitaL
        Teacher.__init__(self, fio, stj, namepr, numstd)

    def findCapitalcity(self):
        if self.capitaL==("Кыргызстан"):
            return ("Бишкек")
        elif self.capitaL==("Германия"):
            return ("Берлин")
        elif self.capitaL==("Турция"):
            return ("Анкара")
        elif self.capitaL=='Россия':
            return ("Москва")
        elif self.capitaL==("Украина"):
            return ("Киев")

    def display(self):
        return self.fio,self.stj,self.namepre,self.numstd, self.findCapitalcity()

teacher1=DrawingTeacher('Askat',22,"География",25, "Круг")
print(teacher1.display())

#Task2
class MathGeographyTeacher:
    def __init__(self,namе):
        self.name=namе
        # self.age=age
        # set.subject.subject
    def display(self):
        print (self.name)
    def introducing(self):
        print (f'Меня зовут {self.name} и я веду Математику и Географию')
    def display(self):
        return (self.name,self.introducing())

class MathTeacher(MathGeographyTeacher):
    def display(self):
        return (self.name,self.introducing())
class GeographyTeacher(MathGeographyTeacher):

    def display(self):
        return (self.name,self.introducing())
G=GeographyTeacher("Asan")
G.display()
M=MathTeacher("Aibek")
M.display()
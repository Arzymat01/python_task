class Xerocopy:
    def __init__(self,nameModel,nameDoc,copyQuanity,copyLimit):
        self.nameModel=nameModel
        self.nameDoc=nameDoc
        self.Quanity=copyQuanity
        self.Limit=copyLimit
    def copy(self):
        self.Limit-=self.Quanity
        return (f'Mодель {self.nameModel} скопировал {self.nameDoc} количестово {self.Quanity} шт остолась {self.Limit}')
    def addLists(self,list_add):
        list_Xero=self.Limit
        self.Limit +=list_add
        return (f'У вас на копировальном аппарате было {list_Xero} листов, после пополнения стало {self.Limit} листов')
    def PrintColored(self,colored):
        colored=self.Limit
        self.Limit -= self.Quanity
        return (f'«Модель {self.nameModel} расспечатал документ {self.nameDoc} в ЦВЕТНОМ варианте в количестве {self.Quanity} шт, осталось {colored} листов»')



class Printer:
    def __init__(self,nameModel,nameDoc,printQuanity,printLimit):
        self.nameModel=nameModel
        self.nameDoc=nameDoc
        self.Quanity=printQuanity
        self.Limit=printLimit
    def PrintBlacked(self):
        self.Limit-=self.Quanity
        return (f'«Модель {self.nameModel} распечатал документ {self.nameDoc} в количестве {self.Quanity} шт, осталось {self.Limit} листов»')
    def addLists(self):
        self.Limit+=self.Quanity
        print(f'У вас на печатном аппарате было {self.Quanity} листов, после пополнения стало {self.Limit} листов')
    def PrintColored(self):
        self.Limit -= self.Quanity
        return (
            f'«Модель {self.nameModel} расспечатал документ \"{self.nameDoc}\" в ЦВЕТНОМ варианте в количестве {self.Quanity} шт, осталось {self.Limit} листов»')


class LGT(Xerocopy,Printer):
    def __init__(self,nameModel,nameDoc,copyQuanity,copyLimit):
        super().__init__(nameModel,nameDoc,copyQuanity,copyLimit)

d=Printer("Canon","Мой отчет",5,15)
print(d.PrintColored())

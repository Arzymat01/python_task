class Xerocopy:

    def __init__(self, nameModel, nameDoc, quanity, limit):
        self.nameModel = nameModel
        self.nameDoc = nameDoc
        self.quanity = quanity
        self.limit = limit

    def copy(self):
        self.limit -= self.quanity
        return (
            f'Mодель {self.nameModel} скопировал документ \"{self.nameDoc}\" количество {self.quanity} шт,остолась {self.limit} листов')

    def addLists(self, list_add):
        lists_in_xero = self.limit
        self.limit += list_add
        return f'У вас на копировальном аппарате было {lists_in_xero} листов, после пополнения стало {self.limit} листов'


class Printer:

    def __init__(self, nameModel, nameDoc, quanity, limit):
        self.nameModel = nameModel
        self.nameDoc = nameDoc
        self.quanity = quanity
        self.limit = limit

    def printBlacked(self):
        self.limit -= self.quanity
        return (
            f'«Модель {self.nameModel} расспечатал документ \"{self.nameDoc}\" в количестве {self.quanity} шт, осталось {self.limit} листов»')

    def PrintColored(self):
        self.limit -= self.quanity
        return (
            f'«Модель {self.nameModel} расспечатал документ \"{self.nameDoc}\" в ЦВЕТНОМ варианте в количестве {self.quanity} шт, осталось {self.limit} листов»')

    def addLists(self, list_add):
        lists_in_printer = self.limit
        self.limit += list_add
        return f'У вас на печатном аппарате было {lists_in_printer} листов, после пополнения стало {self.limit} листов'


class LGT(Xerocopy, Printer):

    def __init__(self, nameModel, nameDoc, quanity, limit):
        super().__init__(nameModel, nameDoc, quanity, limit)


d = LGT("Canon", "Мой отчет", 5, 15)
print(d.copy())
print(d.addLists(3))
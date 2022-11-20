#Task1
class Animal:

    def __init__(self, type_animal, sound):
       self.type_animal = type_animal
       self.sound = sound
    def makeNoice(self):

      print(self.sound)
dog = Animal('Dog', 'Aw-aw')
cat = Animal('Cat', 'Meow')
cow = Animal('Cow', 'Moo-moo')
duck = Animal('Duck', 'Krya-krya')
dog.makeNoice()
cow.makeNoice()
cat.makeNoice()
duck.makeNoice()
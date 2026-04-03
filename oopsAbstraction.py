from abc import ABC , abstractmethod
class animal(ABC):
    
    @abstractmethod
    def hasPart(self):
        pass
        
    @abstractmethod
    def doesPart(self):
        pass

class Dog(animal):
    def hasPart(self):
        print("Tail \n4Legs")
    def doesPart(self):
        print("Barks \nSmell \n")

class Kangaroo(animal):
    def hasPart(self):
        print("pouch \nTail \n2 Legs \nBig Ears")
    def doesPart(self):
        print("Jump \nBoxing \nCarrying baby with it\n")


class Deer(animal):
    def hasPart(self):
        print("Big Horns \nhas white spots")
    def doesPart(self):
        print("Vegetarian \nJumping \n")

d = Dog()
d.hasPart()
d.doesPart()

k = Kangaroo()
k.hasPart()
k.doesPart()


de = Deer()
de.hasPart()
de.doesPart()















        

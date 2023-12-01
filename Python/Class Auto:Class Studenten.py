class Auto:
    def __init__(self,farbe,nummer):
        self.nummer=nummer
        self.farbe=farbe 
    def drive(self):
        print (f"Die Farbe des Autos (Nummer {self.nummer}) ist {self.farbe}")
        
c = Auto ("rot",23)
c.drive()

class Student:
    "Beschreibung einer Studenten"
    anzahl=0
    def __init__(self, name):
        self.name = name
        Student.anzahl +=1
    def getName(self):
        return self.name
    @classmethod
    def getAnzahl(cls):
        return cls.anzahl
    
person1 = Student("Alex")
person2 = Student("Kevin")
person3 = Student("Frank")
print("Hier ist " + person1.getName())
print("Hier ist " + person2.getName())
print("Hier ist " + person3.getName())
print("Anzahl Studenten =", Student.getAnzahl())
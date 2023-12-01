def backe(temperature, mode):
    Anweisungsblock
    
ofentemperatur =180
ofenmodus = 2
backe(ofentemperatur, ofenmodus)

ofentemperaturen = []
ofenmodi = []
ofentemperaturen.append(180)
ofenmodi.append(2)

for i in range (len(ofentemperaturen)):
    backe(ofentemperaturen[i], ofenmodi[i])

class Ofen:
    def __init__(self, temperatur, modus):
        self.temperatur=temperatur
        self.modus=modus
    def backe(self):
        Anweisungsblock
meinOfen=Ofen(180,2)
meinOfen.backe()

ofenliste = []
ofenliste.append(Ofen(180,2))

for Ofen in ofenliste:
    Ofen.backe()
    
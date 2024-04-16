class Ship:
    def __init__(self, jmeno, posadka):
        self.jmeno = jmeno
        self.posadka = posadka

    def showMsg(self):
        return (f"Nazev Lodi: {self.jmeno}, Posádka: {self.posadka}")


class Frigate(Ship):
    def __init__(self, jmeno, posadka, rychlost):
        super().__init__(jmeno, posadka)
        self.rychlost = rychlost

    def showMsg(self):
        return (f"{super().showMsg()}, Rychlost je: {self.rychlost} uzlů")


class Destroyer(Ship):
    def __init__(self, jmeno, posadka, torpeda):
        super().__init__(jmeno, posadka)
        self.torpeda = torpeda

    def showMsg(self):
        return (f"{super().showMsg()}, Počet torpéd: {self.torpeda} ")


class Cruiser(Ship):
    def __init__(self, jmeno, posadka, vyzbroj):
        super().__init__(jmeno, posadka)
        self.vyzbroj = vyzbroj

    def showMsg(self):
        return (f"{super().showMsg()}, Výzbroj: {self.vyzbroj} kanónu ")

frigate1 = Frigate("Alois", 50, 10)
print(frigate1.showMsg())

destroyer1 = Destroyer("Mucha",250, 8 )
print(destroyer1.showMsg())

cruiser1 = Cruiser("Panama",250, 5 )
print(cruiser1.showMsg())


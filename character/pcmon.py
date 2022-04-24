
class Grassy():
    def __init__(self) -> None:
        self.information = {
            "HP Endurance" : 40,
            "Experience" : 10,
            "Defence" : 30,
            "Heal Speed" : 40,
            "Power" : 23
        }

        self.abilities = []

        self.description = "A great all rounder, and the Original PCMon!"
        
        self.abilities.append("Tackle")
        if self.information["Experience"] >= 10:
            self.abilities.append("Cry")
        elif self.information["Experience"] >= 20:
            self.abilities.append("Dirt Smother")
    def getAbilities(self) -> list: return self.abilities
class Wassy():
    def __init__(self) -> None:
        self.information = {
            "HP Endurance" : 30,
            "Experience" : 11,
            "Defence" : 55,
            "Heal Speed" : 20,
            "Power" : 28
        }

        self.abilities = []

        self.description = "\"It's wet!\", jokes aside, a flexible and defensive PCMon."

        self.abilities.append("Splash")
        if self.information["Experience"] >= 20:
            self.abilities.append("Drown")
        elif self.information["Experience"] >= 40:
            self.abilities.append("Corrode")
    def getAbilities(self) -> list: return self.abilities
class Fissy():
    def __init__(self) -> None:
        self.information = {
            "HP Endurance" : 40,
            "Experience" : 15,
            "Defence" : 10,
            "Heal Speed" : 60,
            "Power" : 45
        }

        self.abilities = []

        self.description = "It will burn everything to the ground."

        self.abilities.append("Scorch")
        if self.information["Experience"] >= 12:
            pass
        if self.information["Experience"] >= 23:
            pass
    def getAbilities(self) -> list: return self.abilities
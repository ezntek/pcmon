class PCMon:
    def __init__(self):
        self.HPEndurance = 0 #int
        self.defence = 0 # int
        self.xp = 0
        self.healspeed = 0 # int
        self.abilities = []
        self.name = "" # string

class Grassy(PCMon):
    def __init__(self):
        self.HPEndurance = 40
        self.defence = 30
        self.healspeed = 45
        self.xp = 10

        self.abilities.append("Tackle")

        if self.xp >= 10:
            self.abilities.append("Cry")
        elif self.xp >= 20:
            self.abilites.append("Dirt Smother")

class Wassy(PCMon):
    def __init__(self):
        self.HPEndurance = 30
        self.defence = 55
        self.healspeed = 20
        self.xp = 11

        self.abilities.append("Splash")

        if self.xp >= 15:
            pass
        if self.xp >= 35:
            pass

class Fissy(PCMon):
    def __init__(self):
        self.HPEndurance = 40
        self.defence = 10
        self.healspeed = 60
        self.xp = 15

        self.abilities.append("Scorch")

        if self.xp >= 10:
            pass
        if self.xp >= 17:
            pass

class Yoper(PCMon):
    def __init__(self):
        self.HPEndurance = 10
        self.defence = 10
        self.healspeed = 70
        self.xp = 10

        self.abilities.append("Yoghurt")

        if self.xp >= 20:
            pass

# addition of bocave in later version


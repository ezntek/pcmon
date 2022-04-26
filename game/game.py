from gameio.dataio import DataIO
from gameplay import Gameplay
import time
from con import Console
from character.pcmon import Grassy, Wassy, Fissy

pcmons = [Grassy(), Wassy(), Fissy()]
pcnames = ["Grassy", "Wassy", "Fissy"]
class Character:
    def __init__(self) -> None:
        self.health = 100
        self.scoreCount = 0
        self.activePCMon = 0
        self.coins = 100
        self.disks = 5

    def printData(self):
        print ("HP: {}, Score: {}, Active pcmons: {}, Coins Gained: {},Disk Owned{}")
        return self.health, self.scoreCount, self.activePCMon, self.coins,self.disk
class Game:
    def __init__(self) -> None:
        self.player = Character()
        self.retvals = None
        self.queries = None

    def initNewPlayer(self):
        print("You haven't seemed to play this game before. Lets Pick you a PCMon!")

        for i in range(0, len(pcmons)):
            print(pcnames[i]+":\n")
            print(pcmons[i].information+"\n---")

        while True:
            c = input("pick a pcmon: ")
            if c not in pcnames:
                print("enter a valid choice.")
            else:
                print("congradulations on owning your very own {}".format(c))
                break
        

    def startGame(self):
        self.retvals = DataIO().loadPCMon()
        if self.retvals is False:
            Game().initNewPlayer()

        for i, el in enumerate(self.retvals):
            print((i + 1) + '. ', el)
        while True:
            self.queries = input('What\'s your pick?: ')
            if self.queries not in self.retvals:
                print('Please enter a valid choice!')
            else:
                if self.queries == pcnames[0]:
                    mon = Grassy()
                elif self.queries == pcnames[1]:
                    mon = Wassy()
                elif self.queries == pcnames[2]:
                    mon = Fissy()
                lis = DataIO.readPCMetadata()
                mon.information['Experience'] += int(lis[0])
                mon.information['Power'] += int(lis[1])
                Gameplay().start(mon)
        

from gameio.dataio import DataIO
from con import Console
import time
class Character:
    def __init__(self) -> None:
        self.health = 100
        self.scoreCount = 0
        self.activePCMon = 0
        self.coins = 100
        self.disks = 5

    def printData(self):
        print("HP: {}, Score: {}, Active pcmons: {}, Coins Gained: {},Disk Owned{}")
        return self.health, self.scoreCount, self.activePCMon, self.coins,self.disk

class Game:
    def __init__(self) -> None:
        self.player = Character()
        self.retvals = None

    def initNewPlayer(self):
        print("You haven't seemed to play this game before. Lets Pick you a PCMon!")

    def startGame(self):
        self.retvals = DataIO().loadPCMon()
        if self.retvals is False:
            Game.initNewPlayer()
            


import os, sys
from typing import Union

from sqlalchemy import false
from con import Console

class DataIO:
    def __init__(self) -> None:
        self.readFile = []
        self.temp

    def deposit(self, amount) -> Union[bool, float]:
        try:
            if (not os.path.exists(".pcwallet")):
                open(".pcwallet", "w")
                return True
            with open(".pcwallet") as wallet:
                self.temp = wallet.read()
                wallet.write(str(float(self.temp) + float(amount)))
        except FileNotFoundError:
            return False

    def withdraw(self) -> float:
        try:
            with open(".pcwallet") as wallet:
                return float(wallet.read())
        except FileNotFoundError:
            return False

    def loadPCMon(self):
        if os.path.exists('.pclist'):
            with open('.pclist') as pcmonList:
                for line in pcmonList.readlines():
                    self.readFile.append(line)
                self.readFile = []
                return self.readFile
        elif not os.path.exists('.pclist'):
            return False

    def writePCMonFile(self) -> bool:
        pass
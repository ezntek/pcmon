import os, sys
from typing import Union

class DataIO:
    def __init__(self) -> None:
        self.readFile = []
        self.temp = None

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

    def withdraw(self) -> Union[bool,float]:
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

    def getLogIn(self) -> Union[str, bool]:
        if os.path.exists('.pclogin'):
            with open('.pclogin') as loginFile:
                return loginFile.read()
        elif not os.path.exists('.pclogin'):
            return False

    def saveLogin(self, login) -> bool:
        if not os.path.exists('.pclogin'):
            with open ('.pclogin') as loginFile:
                loginFile.write(str(login))
                return True
        elif os.path.exists('.pclogin'):
            return False

    def writePCMonFile(self) -> bool:
        pass

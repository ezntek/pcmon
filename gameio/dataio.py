import os, sys, json
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

    def loadPCMon(self) -> Union[list, bool]:
        try:
            with open('.pclist') as list:
                mons, retvals = []
                mons = list.readlines()
                dictionary = json.loads('pcmonID.json')
                for item in mons:
                    retvals.append(dictionary[str(item)])
                return retvals
        except FileNotFoundError:
            return False
    
    def returnPCJson(self) -> Union[dict, bool]:
        try:
            with open('pcmonID.json') as jsn:
                return json.loads(jsn.readlines())
        except FileNotFoundError:
            return False
    
    def saveNewPCMon(self, id) -> bool:
        try:
            with open('.pclist') as file:
                file.write(str(id)+"\n")
                return True
        except FileNotFoundError:
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

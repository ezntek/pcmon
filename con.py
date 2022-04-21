import os
import sys

class ConCommands:
    def __init__(self) -> None:
        commandList = [
            "exit",
            "clear",
            "game"
        ]

class Console:
    def __init__(self) -> None:
        self.retvals = None

    def log(p):
        print("\n ls()log: {}\n".format(p))

    def parseCommand(cmd) -> bool:
        if (cmd[0] not in ConCommands().commandList):
            return False
        else:
            if (cmd[0] == ConCommands().commandList[0]):
                if (cmd[1] == "0"):
                    sys.exit(0)
                elif (cmd[1] == "1"):
                    sys.exit(1)
            if (cmd[0] == ConCommands().commandList[1]):
                os.system("clear")
            if (cmd[0] == ConCommands().commandList[2]):
                pass

    def prompt(self):
        while True:
            commandInput = input("pcmon_debug> ")
            cmd = tuple(commandInput.split(" ")[:-1])
            self.retvals = parseCommand(cmd)

            if (self.retvals == False):
                Console.log("please enter a valid command.")

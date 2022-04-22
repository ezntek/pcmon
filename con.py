import os
import sys

class Console:
    def __init__(self):
        self.retvals = None
        self.commandList = [
            "exit",
            "clear",
            "game"
        ]

    def log(p):
        print("\n ls()log: {}\n".format(p))

    def parseCommand(command, self) -> bool:
        cmd = command.strip(' ').split(' ')
        Console.log(cmd)
        if cmd[0] not in self.commandList:
            return False
        else:
            if (cmd[0] == self.commandList[0]):
                if (cmd[1] == "0"):
                    sys.exit(0)
                elif (cmd[1] == "1"):
                    sys.exit(1)
            if (cmd[0] == self.commandList[1]):
                os.system("clear")
            if (cmd[0] == self.commandList[2]):
                pass

    def prompt(self):
        while True:
            commandInput = input("pcmon_debug> ")
            print(commandInput)
            self.retvals = Console().parseCommand(commandInput)

            if (self.retvals == False):
                Console.log("please enter a valid command.")


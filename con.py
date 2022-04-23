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

    def log(p): print("\nlog> {}\n".format(p))

    def parser(self, command):
        cmd = command.strip(' ').split(' ')
        if cmd[0] not in self.commandList:
            return False
        else:
            if cmd[0] == self.commandList[0]:
                if int(cmd[1]) > 1:
                    print('placeholder')
                else:
                    sys.exit(int(cmd[1]))
            if cmd[0] == self.commandList[1]:
                os.system('clear')
            if cmd[0] == self.commandList[2]:
                Console.log('placeholder')


    def prompt(self):
        while True:
            c = input('pcmon_console> ')
            self.retvals = Console().parser(c)
            if self.retvals is False:
                Console.log('the command had failed to run.')



import os
import sys

class ConCommands:
    def __init__(self) -> None:
        self.usages = {
            "exit" : "exit <0(no error code) or 1(error)>"
        }
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
                try:
                    if int(cmd[1]) > 1:
                        print('placeholder')
                    elif cmd[1] == "catsAreNice":
                        Console.log('~meow!~')
                        sys.exit(0)
                    else:
                    #self.gamestate==False
                        sys.exit(int(cmd[1]))
                except IndexError:
                    Console.log(ConCommands().usages["exit"])
            if cmd[0] == self.commandList[1]:
                os.system('clear')
            if cmd[0] == self.commandList[2]:
                from game.game import Game
                Game().startGame()


    def prompt(self):
        while True:
            c = input('pcmon_console> ')
            self.retvals = Console().parser(c)
            if self.retvals is False:
                Console.log('the command had failed to run.')



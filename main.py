import sys
from con import Console

class Main:
    def __init__(self) -> None:
        self.choices = None
        self.vers = "alpha 6"

    def main(self):
        print("pcmon {}".format(self.vers))
        print("menu [con] [exit] [creators]")
        self.choices = input(": ")

        if (self.choices == "con"):
            Console().prompt()
        if (self.choices == "exit"):
            sys.exit(0)
        if (self.choices == "creators"):
            print("PCMon was originally written by meowscripty in November of 2021,\n"+
            "and the creator, easontek2398 and meowscripty himself are bringing a project from humble\n"+
            "origins back to life.\n\n"+
            "easontek2398, meowscripty")

if __name__ == "__main__": 
    Main().main()

import sys
from con import Console

class Main:
    def __init__(self) -> None:
        self.choices = None
        self.vers = "0.0 test"

    def main(self):
        print("pcmon debug {}".format(self.vers))
        print("menu [con] [exit] [creators]")
        self.choices = input(": ")

        if (self.choices == "con"):
            Console().prompt()

if __name__ == "__main__": Main().main()

import os, sys

class DataIO:
    def __init__(self) -> None:
        pass

    def Deposit(self, x) -> bool:
        if (not os.path.exists(".pcwallet")):
            open(".linerwallet", "w")



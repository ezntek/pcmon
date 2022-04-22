from gameio.dataio import DataIO
class PCdiskATM:
    def __init__(self):
        self.baldisk = None

class PCCoinATM:
    def __init__(self) -> None:
        self.balance = None
        self.login = False

    def login(self):
        code = DataIO().getLogIn()

        if code is False:
            print('You need to set a password fist.')
            return
        
        for i in range(0, 3):
            codeInput = input("Enter your passcode.")
            if codeInput != code:
                if i == 3:
                    print("you tried to enter the wrong passcode too many times, please try again later.")
                print('you entered the wrong passcode. try again.')
            elif codeInput == code:
                self.login = True
                print('login success.')
        

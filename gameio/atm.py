from gameio.dataio import DataIO
from con import Console

class PCdiskATM:
    def __init__(self):
        self.baldisk = None

class PCCoinATM:
    def __init__(self) -> None:
        self.login = False
        self.retval = None
        self.retval = DataIO().withdraw()
        if self.retval is False:
            Console.log('fatal error fileNotFoundError')
            pass
        else if type(self.retval) == float:
            self.balance = self.retval
            self.retval = None

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

    def openAccount(self):
        code = input('Enter a passcode to set')
        verify = None

        try:
            while not verify == code:
                verify = input('Enter the code again to verify.')
                if not verify == code:
                    print('The codes do not match!')
                else:
                    break
        except KeyboardInterrupt:
            print('restarting prompt.')
            PCCoinATM().openAccount()

        self.retval = DataIO().saveLogin(verify)
        if self.retval is False:
            print('a code exists.')

    def withdraw(self):
        self.retval = DataIO().withdraw()
        if self.retval is False:
            print('fatal error filenotfound')
        else if type(self.retval) == float:
            self.balance += self.retval
            self.retval = None



import os

class ModSetup:
    def __init__(self):
        self.find = os.path.exists(".modfolder")
    
    def modFinder(self):
        with open(self.find) as f:
            self.mod_finding = f.read()
            if self.mod_finding:
                try:
                    with open(self.mod_finding) as fu:
                        self.modfound = fuu.read()
                except:
                    raise AssertionError
            else:
                self.mod_exist=False

if __name__ == "__main__":   
    u=ModSetup()
    u.modFinder()
else:
    print("why are u running this? play the game to install mods.")

        
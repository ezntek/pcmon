import os

class mod_setup:
    def __init__(self):
        self.find = os.path(".modfoder")
    
    def modFinder(self):
        with open(self.find) as f:
            self.mod_finding = f.read()
            if self.mod_finding:
                try:
                    with open(self.mod_finding) as fu:
                        self.modfound = f.read()
                except:
                    raise AssertionError
                    

        
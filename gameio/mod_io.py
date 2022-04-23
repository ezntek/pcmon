import os
import pygame
import sys #wtf no this is a console game
class ModSetup:
    def __init__(self):
        self.find = os.path.exists(".modfolder")
    
    def modFinder(self):
        try:
            with open(self.find) as f:
                self.mod_finding = f.read()
                if self.mod_finding:
                    try:
                        pass
                    except:
                        print("can't load mod")
                        raise AssertionError
                else:
                    self.mod_exist=False
        except FileNotFoundError:
            pass
            

    def fileclosing(self, f):
        if pygame.events=="Quit": # This is pygame events, not console events, i think im bteter at python than you bruh
            f.close()
        else:
            sys.exit()
 

if __name__ == "__main__":   
    u=ModSetup()
    u.modFinder()
else:
    print("---by meowscripty---\n"+"why are u running this? play the game to install mods.")

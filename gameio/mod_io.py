import os,sys,con
class ModSetup(con):
    def __init__(self):
        self.find = os.path.exists(".modfolder")
        self.getname=os.path.getname("self.find")
    def modFinder(self):
        try:
            with open(self.find) as f:
                self.mod_finding = f.read()
                if self.mod_finding:
                    try:
                        pass
                        #from self.getname import self.mod_finding
                    except:
                        print("can't load mod")
                        raise AssertionError
                else:
                    self.mod_exist=False
        except FileNotFoundError:   
            print("file can't open")
            

    def fileclose(self, f, con): 
           if self.gamestate==False:
            f.close()
             
            
                
if __name__ == "__main__":
    u=ModSetup()         
    u.modFinder()
else:
    print("---by meowscripty---\n"+"why are u running this? play the game to install mods.")

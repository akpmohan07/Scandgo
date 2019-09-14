import packages.database.distribute as distribute
import packages.database.collect as collect
import packages.gui.home as gui
from tkinter import filedialog
from tkinter import *
import os

path=os.getcwd()+"\output_path.txt"
file=open(path,"r+")
output_path=file.readline()
if output_path=="NULL":
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    file.seek(0)
    file.write(folder_selected)
file.close()
gui.home()






   





    
    

        




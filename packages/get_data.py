import packages.qrscan.webcam.webcam as wc
import pandas as pd
import packages.gui.popup as pu
import tkinter as tk
import packages.date_time as gt

path="D:\scandgo"
def distribute_scanner(location):
	value = []
	rollno=  wc.webcam("Scan your ID card")
	if(rollno=="Scanner Terminated"):
		return 0
	check = check_roll_conflict(rollno,location)
	if check==0:
		pu.distribute_roll_conflict(rollno)
		return "conflict"
	title = rollno+" -Scan your Laptop"
	sys_number = wc.webcam(title)
	check1 = check_sys_conflict(sys_number,location)
	if check1==0:
		pu.distribute_sys_conflict(sys_number)
		return "conflict"
	value.append(rollno)
	value.append(sys_number)
	return value
def collect_scanner():
	sys_number = wc.webcam("Scan your Laptop")
	if(sys_number=="Scanner Terminated"):
		return 0
	return sys_number

def get_name(roll_no):
	df = pd.read_excel(r'D:\scandgo\class_data.xlsx')
	df.set_index("Roll_No", inplace=True)
	return df.loc[roll_no,'Name']

def check_roll_conflict(roll_no,location):
	df1 = pd.read_excel(location)
	roll=list(df1["Roll_No"])
	if (roll_no in roll):#Roll_No already bought a laptop
		return 0
	else:
		return 1

def check_sys_conflict(sys_no,location):
	df1 = pd.read_excel(location)
	sysno=list(df1["System_No"])
	if (sys_no in sysno):#Laptop already Distributed.
		return 0
	else:
		return 1

def class_code():
    global x,y,z
    window = tk.Tk()
    window.title("Class Code")
    current_year=int(gt.dates()[8:])
    start_year = current_year-4
    year = []
    for i in range(0,5):
        year.append(start_year)
        start_year+=1
    department = ["CS","IT","EC","EE","CV","MC","MT"]
    section = ["A","B","C"]
    yr = tk.StringVar()
    yr.set("Year")
    dep = tk.StringVar()
    dep.set(department[0])
    sec = tk.StringVar()
    sec.set(section[0])
    
    
    yr_menu = tk.OptionMenu(window,yr,*year)
    yr_menu.pack()
    dep_menu = tk.OptionMenu(window,dep,*department)
    dep_menu.pack()
    sec_menu = tk.OptionMenu(window,sec,*section)
    sec_menu.pack()
    
    
    def on_click():
        global x,y,z
        x = yr.get()
        y = dep.get()
        z = sec.get()
        window.destroy()
    
    
    button = tk.Button(window,text='OK',command= on_click)
    button.pack()
    window.mainloop()
    data = x+y+z
    return data
	

	
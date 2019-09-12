import tkinter as tk
import packages.database.distribute as distribute
import packages.database.collect as collect
import packages.get_data as gd
def home():
	home = tk.Tk()
	home.title("Home")
	distribute_button = tk.Button(home,text="Distribute",command=call_distribute)
	distribute_button.pack()

	collect_button = tk.Button(home,text="Collect",command=call_collect)
	collect_button.pack()

	button = tk.Button(home,text='OK',command= home.destroy)
	button.pack()

	home.mainloop()
def call_distribute():
	distribute.write(gd.class_code())
def call_collect():
	collect.write(gd.class_code())

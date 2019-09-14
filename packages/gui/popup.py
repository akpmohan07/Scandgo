import os
import tkinter as tk  
from tkinter import messagebox  
  
def distribute_roll_conflict(msg):
	messagebox.showwarning("warning!",msg+"--Already bought a laptop.")  

def distribute_sys_conflict(msg):
	messagebox.showwarning("warning!",msg+"--Already Distributed.")
	  
def collect_sysnd_conflict(msg):

	messagebox.showwarning("Warning",msg+"--Not Distributed")

def collect_sysac_conflict(msg):
	messagebox.showwarning("warning!",msg+"--Already Collected.")
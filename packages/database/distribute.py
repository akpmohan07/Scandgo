import pandas as pd
import packages.get_data as gd
import packages.date_time as dt
import packages.gui.popup as pu

import numpy as np


def write(class_code):
	
	file_name = dt.dates()+"-"+class_code[0]+class_code[1]+"-"+class_code[2]+class_code[3]+"-"+class_code[4]+".xlsx"
	location = gd.output_path() +"/E-"+ file_name
	data = []
	df1 = pd.DataFrame({'S.No':[],'Roll_No':[],'Name':[],'System_No':[],'Date':[],'In_Time':[],'Out_Time':[],'Status':[]})
	df2 = pd.DataFrame({'S.No':[],'Roll_No':[],'Name':[],'System_No':[],'Date':[],'In_Time':[],'Out_Time':[],'Status':[]})
	writer = pd.ExcelWriter(location)
	df1.to_excel(writer,startrow=0,header=True,index=False)
	writer.save()
	i=1
	roll=[]
	sysno=[]
	
	
	
	while True:
		data = gd.distribute_scanner(location)
		if data==0:
			break
		if data=="conflict":
			continue
		roll_no = data[0]
		sys_number = data[1]
		if (sys_number=="Scanner Terminated"):
			continue
		roll=list(df1["Roll_No"])
		sysno=list(df1["System_No"])
		if (sys_number in sysno):#system already distributed
			continue
		if (roll_no in roll):#Roll_No already bought a laptop
			continue
		namee = gd.get_name(roll_no)
		datee = dt.dates()
		timee = dt.times()
		df1 = pd.DataFrame({'S.No':[i],'Roll_No':[roll_no],'Name':[namee],'System_No':[sys_number],'Date':[datee],'In_Time':[timee],'Out_Time':[None],'Status':["NotReturned"]})
		df1.to_excel(writer,startrow=i,header=False,index=False)
		i=i+1
		writer.save()
		df2=df2.append(df1,ignore_index = True)
	df2.index = np.arange(1, len(df2) + 1)

	
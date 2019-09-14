import pandas as pd
import packages.get_data as gd
import packages.date_time as dt
import numpy as np
import packages.gui.popup as pu

def write(class_code):
	file_name = dt.dates()+"-"+class_code[0]+class_code[1]+"-"+class_code[2]+class_code[3]+"-"+class_code[4]+".xlsx"
	location = gd.path +"\E-"+ file_name
	df = pd.read_excel(location)
	writer = pd.ExcelWriter(location)
	#df.to_excel(writer,index=False)
	sysno=[]
	sysno=list(df["System_No"])
	
	
	
	while True:
		key = gd.collect_scanner()
		if key==0:
			break
		
		if key not in sysno:#system not distributed
			pu.collect_sysnd_conflict(key)
			continue
		df.set_index("System_No",inplace=True)
		if df.loc[key,'Status'] == "Returned":#system already collected
			pu.collect_sysac_conflict(key)
			df=df.reset_index()
			continue

		timee = dt.times()
		
		df.loc[key,'Out_Time'] = timee
		df.loc[key,'Status'] = "Returned"
		df=df.reset_index()
		
		
		df=df[["S.No","System_No","Roll_No","Name","Date","In_Time","Out_Time","Status"]]
		df.to_excel(writer,index=False)
		writer.save()



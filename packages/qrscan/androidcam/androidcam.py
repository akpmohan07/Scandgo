import requests,cv2,winsound
import pyzbar.pyzbar as pyzbar
import numpy as np
def androidcam():
	frequency = 2100
	duration = 700
	flag=0
	value = "Scanner terminated"
	url="http://192.168.137.97:8080/photo.jpg"
	while True:
	    res = requests.get(url)
	    img_array = np.array(bytearray(res.content),dtype=np.uint8)
	    img = cv2.imdecode(img_array,5)
	    
	    decode = pyzbar.decode(img)
	    for obj in decode:
	        data = str(obj.data)
	        value=data[2:int(len(data))-1]
	        winsound.Beep(frequency,duration)
	        flag=1
	    if (flag==1):
	        cv2.destroyAllWindows()
	        break
	    q = cv2.waitKey(1)
	    if q == ord("q"):
	        break;
	    return value


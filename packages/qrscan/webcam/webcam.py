import requests,cv2,winsound
import pyzbar.pyzbar as pyzbar
import numpy as np

def webcam(title):
    frequency = 2100
    duration = 700
    flag=0
    value = "Scanner Terminated"

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        decode = pyzbar.decode(frame)
        for obj in decode:
            data = str(obj.data)
            value=data[2:int(len(data))-1]
            winsound.Beep(frequency,duration)
            flag=1
        
        if (flag==1):
            cv2.destroyAllWindows()
            break
        cv2.imshow(title,frame)
        q = cv2.waitKey(1) 
        if q == ord("q"):
            break
    return value

   
    
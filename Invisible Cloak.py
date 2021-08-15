import numpy as np
import cv2 
import time
cap=cv2.VideoCapture(0)#Read from the default web cam i.e why 0

time.sleep(3) #for the system to sleep for 3 second before the webcam starts
for i in range(30):
    retval,back=cap.read()
back=np.flip(back,axis=1) #images captured is mirror image so we need to flip it again to get the original background amd axis=1 means laterally invert image
cap=cv2.VideoCapture(0)  



## detecting the red portion In each frame


while (cap.isOpened()):  ##Read every Frame from the webcam, until the camera is open 
    ret,img=cap.read()
    if ret:
        img=np.flip(img,axis=1)
        
        ##convert the color space from BGR to HSV because BGR  cant detect colour efficiently
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        ##Generat masks to detect red color
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv,lower_red,upper_red)
        
        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        mask1+=mask2
        
        ###Replacing the red portion with a mask image in each frame

        mask = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
        img[np.where(mask==255)]=back[np.where(mask==255)]
        
         #Final output
        cv2.imshow("Harry Potter's invisible secret revealed",img)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

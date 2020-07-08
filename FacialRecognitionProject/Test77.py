''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18  

'''
from notiFy import sendNoti
import cv2
import numpy as np
import os
from mail import sendMail
import sqlite3
from employee import Employee
import time
from imutils.video import VideoStream
import imutils
from sohilPyrebase import sendmsg
from getnames import getstdname
from parentMail import getParentMail

conn = sqlite3.connect(':employee.db')

c = conn.cursor()

def printid(id):
    print(id)
    
    
def printi(emps):
    print(emps)



def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def get_emps_by_id(id):
    c.execute("SELECT last FROM employees WHERE pay=:pay", {'pay': id})
  
    for row in c.fetchall():
        print(row[0])
    return (row[0])

recognizer =cv2.createLBPHFaceRecognizer()#()
recognizer.load('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
face_detector=cv2.CascadeClassifier(cascadePath);
#faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
d=0
a=-1

# names related to ids: example ==> Marcelo: id=1,  etc
names =getstdname()
#names=['Moin', 'Abdul', 'srijan', 'neha', 'anuya', 'sanjali','test3','abcd','xyz','jkl','sohil'] 
pmail=getParentMail()


#a=99
#printid(a)
#emps = get_emps_by_id(a+1)
#emps=pmail.get(str(a))
#print(emps)
#sendMail(emps)
#sendmsg(a)

usingPiCamera = False
frameSize = (480,480)

dim = (480,480)
cam = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
		framerate=32).start()
# Initialize and start realtime video capture
#cam = cv2.VideoCapture(0)
#cam.set(3, 640) # set video widht
#cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
#minW = 0.1*cam.get(3)
#minH = 0.1*cam.get(4)

time.sleep(2.0)#added
allid=[]
timeCheck = time.time()#added
count=0
while (True):

    img =cam.read()
   # img = cv2.flip(img, -1) # Flip vertically
    
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img, 1.3, 5)
    #faces = faceCascade.detectMultiScale( 
     #  gray,
      #  scaleFactor = 1.2,
      # minNeighbors = 5,
      # minSize = frameSize #(int(minW), int(minH)),
      #)
    
    for(x,y,w,h) in faces:
           #print("Here")
           cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
           id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match 
           if (confidence < 100):
               a=id
               allid.append(a)
            #   print("confidence ")
               id = names.get(str(id))#names[id]
               #id=names[id]
               confidence = "  {0}%".format(round(100 - confidence))
               count+=1 
               detect=True
               
           else:
               id = "unknown"
               confidence = "  {0}%".format(round(100 - confidence))
               count+=1
               detect=False
           
           cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
           cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
           #i+=1
        
    cv2.imshow('camera',img)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('786image.jpg',resized)


    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 2:
       
        break
    if count>8:
            break


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

#cam.stream.release()

final_list = [] 
for num in allid: 
    if num not in final_list: 
        final_list.append(num) 
print(final_list)
for a in final_list:
    if(a>=0 and detect):
        print(names.get(str(a)))
        #emps = get_emps_by_id(a+1)
        emps=pmail.get(str(a))
        #print(emps)
        sendNoti()
        #sendMail(emps)
        sendmsg(a)
    
  
cv2.destroyAllWindows()
conn.close()


















##emps = get_emps_by_name('Doe')
##print(emps)



  






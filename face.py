import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #Importing Haarcascade classifier
cap=cv2.VideoCapture(0) #capturing the vide frames

print(cv2.__file__)

while (True):
    ret,frame=cap.read() #reading each frames in the video cam
    print(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        #converting to gray for detecting the faces
    faces=face_classifier.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)  #printing the face cordinates at each frame
        width=x+h   #end cordinate of x value
        height=y+h  #end cordinate of y value
        color=(0,255,0)
        stroke=5
        cv2.rectangle(frame, (x,y), (width, height), color, stroke)       #Drawing the rectangle 


    cv2.imshow('frame', frame)             #Displaying each frames
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
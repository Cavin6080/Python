import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'images'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)

def findEncodings(images):
    encodlist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encod = face_recognition.face_encodings(img)[0]
        encodlist.append(encod)
    return encodlist

def markAttandance(name):
    with open('attandance.csv','r+') as f:
        myDatalist = f.readlines()
        nameList = []
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')



encodelistforknown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    faceCurrFrame = face_recognition.face_locations(imgSmall)
    encodOfCurrFrame = face_recognition.face_encodings(imgSmall,faceCurrFrame)

    for encodeFace,faceloc in  zip(encodOfCurrFrame,faceCurrFrame):
        matches = face_recognition.compare_faces(encodelistforknown,encodeFace)
        face_dis = face_recognition.face_distance(encodelistforknown,encodeFace)
        #print(face_dis)
        matchIndex = np.argmin(face_dis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttandance(name)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
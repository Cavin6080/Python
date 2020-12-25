import cv2
import numpy as np
import face_recognition

imgTej = face_recognition.load_image_file('images/tej_test.jpeg')
imgTej = cv2.cvtColor(imgTej,cv2.COLOR_BGR2RGB)

imgtest = face_recognition.load_image_file('images/tej.jpeg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(imgTej)[0]
face_encod = face_recognition.face_encodings(imgTej)[0]
cv2.rectangle(imgTej,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(255,0,0),2)

face_loct = face_recognition.face_locations(imgtest)[0]
face_encodt = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(face_loct[3],face_loct[0]),(face_loct[1],face_loct[2]),(255,0,0),2)

face_dis = face_recognition.face_distance([face_encod],face_encodt)
results = face_recognition.compare_faces([face_encod],face_encodt)
cv2.putText(imgTej,f'{results}{round(face_dis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
print(results,face_dis)

cv2.imshow("Tejtest",imgTej)
cv2.imshow("Tej",imgtest)
cv2.waitKey(0)

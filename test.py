import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)
log = open("log.txt","a")
#Check main4.py for more example on use of video sources

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10 )
    haar_cascade = cv2.CascadeClassifier('haar_face.xml')
    people = ['Shreyansh Jaiswal']
    face_recogniser = cv2.face.LBPHFaceRecognizer_create()
    face_recogniser.read('face_trained.yml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Detect the face in the image
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recogniser.predict(faces_roi)
        confidence=100-float(confidence)
        log.write(f'{people[label]} detected with a confidence of {confidence} at time {str(datetime.now())}\n')
        print('Written..')
        cv2.putText(img, str(people[label]), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('Detected Faces', img)
    if cv2.waitKey(20) == ord('q'):
        log.close()
        break

cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

haar_cascade = cv2.CascadeClassifier('haar_face.xml')
people = ['Shreyansh Jaiswal']
img = cv2.imread('assets\test.jpg')
# features = np.load('fatures.npy')
# labels = np.load('labels.npy')
#Use allow_pickle=True to use these but for now these are not necessary

face_recogniser = cv2.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Target', gray)

#Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recogniser.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('Detected Faces', img)

cv2.waitKey(0)
import cv2
import numpy as np
import os

people = ['Shreyansh Jaiswal']

# p = []
# for i in os.listdir(r"G:\ekanfiles\OpenCV-2\assets"):
#     p.append(i)

# print(p)

DIR = 'G:\\ekanfiles\\OpenCV-2\\assets'

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

features = []
labels = []

def train():
    # Loop over every folder in the given directory and the loop over every image
    # present in the directory mentioned and then grab that image and then add that imaeg to the train
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]#roi means reigon of interest 
                features.append(faces_roi)
                labels.append(label)
                #This is done to reduce the strain on our computer by mapping

train()
print('Trainign done')

print(f'Length of the features list is = {len(features)}')
print(f'Length of the labels list is = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recogniser = cv2.face.LBPHFaceRecognizer_create()

#Train the recogniser on the feature list and label list
face_recogniser.train(features,labels)
face_recogniser.save('face_trained.yml')
np.save('fatures.npy', features)
np.save('labels.npy', labels)
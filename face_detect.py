import cv2

cap = cv2.VideoCapture(0)
#Check main4.py for more example on use of video sources

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10 )
    # ''' THe following are the different meanings of the given abbrevations 
    # 10 stands for the line thickness here it is 10 pixels
    # 255,0,0 means the color of the line  
    # 0,0 is the start point of the line 
    # (width, height) is the ending position'''
    #Note that the origin in the vision libraries are mostly 0,0 from top left unlike catresian system
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier('haar_face.xml')
    faces_react = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=10)
    # Note - THe less the value of minNeighbours is the more sensitive is our detector to background noises
    # that implies that  there can be few false detections so we need to mind that
    # but we may use dlib which has even better results 

    print(f'No of faces found is {len(faces_react)}')

    for (x,y,w,h) in faces_react:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv2.imshow('frame', img)

    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
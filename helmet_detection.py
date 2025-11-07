


import cv2
import numpy as np
# Load cascade files
helmet_cascade = cv2.CascadeClassifier("c:\\Users\\Nilesh gupta\\haarcascade_helmet.xml")
face_cascade = cv2.CascadeClassifier("c:\\Users\\Nilesh gupta\\haarcascade_frontalface_default.xml")

# Check if loaded properly
if helmet_cascade.empty():
    print("Error: Helmet cascade not loaded. Check the file path!")
    exit()

if face_cascade.empty():
    print("Error: Face cascade not loaded. Check the file path!")
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    helmets = helmet_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    helmet_found = False

    for (x, y, w, h) in helmets:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        helmet_found = True
        cv2.putText(frame, "Helmet", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    for (x, y, w, h) in faces:
        if not helmet_found:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            flip_video=cv2.flip(frame,1)
            shrpen_kernal=np.array([
                [0,-1,0],
                [-1,5,-1],
                [0,-1,0]
            ])
            Video=cv2.filter2D(flip_video,-1,shrpen_kernal)
            cv2.putText(Video, "No Helmet!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            cv2.putText(flip_video, "No Helmet!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
    cv2.imshow("Helmet ", Video)
    # cv2.imshow("Helmet Detection", flip_video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


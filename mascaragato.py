import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\Barbies\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalcatface.xml')

img = cv2.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gatoD.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for x,y,w,h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
cv2.imwrite('image.jpg', img)
cv2.imshow('foto.jpg',img)
print("Success!")
cv2.waitKey()
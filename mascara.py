import cv2 as cv
import numpy as np

rostros = cv.CascadeClassifier('C:\\Users\\Barbies\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalcatface_extended.xml')

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
gris=cv.cvtColor(original,cv.COLOR_BGR2GRAY)
#cara=rostros.detectMultiScale(gris,
#    scaleFactor=1.1,
#    minNeighbors=1,
#    minSize=(30,30),
#    maxSize=(200,200))

#for(x,y,w,h) in cara:
    #rectangulo=(original,(x,y),(x+w,y+h),(0,255,0),2)
#    cv.circle(original,((x+x+w)/2,(y+y+h)/2) ,(y+y+h)/2,(0,255,0),3)

caras = rostros.detectMultiScale(gris,1.3,5)
for x,y,w,h in caras:
    cv.rectangle(original,(x,y),(x+w,y+h),(255,0,0),7)


#cv.imwrite('foto.jpg',original)
cv.imshow('foto.jpg',original)
cv.waitKey(0)
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\Barbies\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalcatface.xml')

img = cv2.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rectangular_mask = np.zeros(img.shape[:2], dtype='uint8')
cv2.circle(img,(150,150) ,200,(0,255,0),3)
cv2.imshow('MASCARA RECTANGULAR', rectangular_mask)


# Aplicamos la máscara rectangular sobre la imagen de prueba, con el fin de aislar la región
# donde se encuentra el carro.
masked = cv2.bitwise_and(img, img, mask=rectangular_mask)
cv2.imshow('MASCARA RECTANGULAR, RESULTADO', masked)
cv2.waitKey(0)
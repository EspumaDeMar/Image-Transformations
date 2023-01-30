import cv2 as cv

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
shear=original[250:750,120:400]

cv.imshow('Original' , original)
cv.imshow('Parte de la Imagen',shear)
cv.waitKey(0)
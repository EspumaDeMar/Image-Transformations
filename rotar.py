import cv2 as cv

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
noventa=cv.rotate(original,rotateCode=0)

cv.imshow('Original' , original)
cv.imshow('Rotado 90 grados',noventa)
cv.waitKey(0)
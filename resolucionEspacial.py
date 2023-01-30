import cv2 as cv

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')

tamaño=cv.resize(original,(72,72))

cv.imshow('Redimencionado',tamaño)
cv.waitKey(0)
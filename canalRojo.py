import cv2 as cv

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
cv.imshow('Original Image' , original)

rojo = original.copy()

rojo[:,:,0]=0#blue
rojo[:,:,1]=0#gree


#rojo[:,:,2]=16
#rojo1=rojo
#rojo1[:,:,2]=2
cv.imshow('Canal Rojo',rojo)
#cv.imshow('Canal Rojo de intensidad 16',rojo)
#cv.imshow('Canal Rojo de intensidad 2',rojo1)
cv.waitKey(0)
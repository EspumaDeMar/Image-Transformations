import cv2 as cv

original = cv.imread('C:\\Users\\Barbies\\Desktop\\Computacion Visual\\Tareas\\Tarea02\\gato.jpg')
reflejo=cv.flip(original,flipCode=1)#cambaiar el flipcode=0 si quiere un reflejo vertical

cv.imshow('Original' , original)
cv.imshow('Reflejo',reflejo)
cv.waitKey(0)
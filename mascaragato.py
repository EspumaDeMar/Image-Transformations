# Importamos las dependencias del proyecto
import cv2 
import numpy as np

image = cv2.imread('gato.jpg')
cv2.imshow('ORIGINAL', image)
cv2.waitKey(0)

# Ahora creamos una máscara circular y la mostramos en pantalla.
circular_mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(circular_mask, (300, 500), 150, 255, -1)
cv2.imshow('MASCARA CIRCULAR', circular_mask)
cv2.waitKey(0)

# Aplicamos la máscara circular a la imagen de entrada para aislar el logo del gato.
masked = cv2.bitwise_and(image, image, mask=circular_mask)
cv2.imshow('MASCARA CIRCULAR, RESULTADO', masked)
cv2.waitKey(0)

# Destruimos todas las ventanas creadas.
cv2.destroyAllWindows()
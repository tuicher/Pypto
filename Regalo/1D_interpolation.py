import cv2
import numpy as np

w = 800
h = 20

def lerp (color_a, color_b, percent):
    a = color_a * (1 - percent)
    b = color_b * percent
    return a + b;

#Crear una imagen de color negro
img1 = np.zeros((h,w,3),np.uint8)

#Crear una imagen de color blanco
#img2 = 255*np.ones((h,w,3),np.uint8)
#(B,G,R)
left_color = (255, 255, 0)
right_color = (255, 0, 255)


for j in range (w):
    percent = j/w
    blue = lerp(left_color[0], right_color[0], percent) 
    green = lerp(left_color[1], right_color[1], percent) 
    red = lerp(left_color[2], right_color[2], percent)
    for i in range(h):
        if j == 0:
            img1[i,j] = left_color
        if j == w-1:
            img1[i,j]= right_color
        else:
            img1[i,j] = (blue, green, red)

#Mostrar imagen
cv2.imshow('imagen1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

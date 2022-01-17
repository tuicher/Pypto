import cv2
import numpy as np

w = 480
h = 720

def RGB_to_BGR(r, g, b):
    return (b,g,r)

def color_lerp(c, d, percent):
    blue = lerp(c[0], d[0], percent) 
    green = lerp(c[1], d[1], percent) 
    red = lerp(c[2], d[2], percent)
    return (blue, green, red)

def lerp (color_a, color_b, percent):
    a = color_a * (1 - percent)
    b = color_b * percent
    return a + b;

#Creamos una imagen de color negro
img1 = np.zeros((h,w,3),np.uint8)

#(B,G,R)
#top_l_color = (255, 255, 0)
#top_r_color = (255, 0, 255)
#botom_l_color  = (255, 0, 255)
#botom_r_color = (255, 255, 0)

top_l_color = RGB_to_BGR(102, 44, 145)
top_r_color = RGB_to_BGR(23, 163, 152)
botom_l_color  = RGB_to_BGR(51, 49, 46)
botom_r_color = botom_l_color
#botom_r_color = RGB_to_BGR(238, 108, 77)


for j in range (w):
    percent_w = j / w
    for i in range(h):
        percent_h = i / h
        if j == 0 & i == 0:
            img1[i,j] = top_l_color
        if j == w-1 & i == 0:
            img1[i,j]= top_r_color
        if j == 0 & i == h-1:
            img1[i,j] = botom_l_color
        if j == w-1 & i == h-1:
            img1[i,j] = botom_r_color
        else:
            a = color_lerp(top_l_color, top_r_color, percent_w)
            b = color_lerp(botom_l_color, botom_r_color, percent_w)
            img1[i,j] = color_lerp(a, b, percent_h)

#Mostrar imagen
cv2.imshow('imagen1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

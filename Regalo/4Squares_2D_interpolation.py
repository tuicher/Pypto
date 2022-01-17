import cv2
import numpy as np
import random as rnd

# twt resolution = 640x640
w = 640
h = 640

def RGB_to_BGR(r, g, b):
    return (b,g,r)
    
palette = [RGB_to_BGR(229, 153, 52),
    RGB_to_BGR(154, 230, 110),
    RGB_to_BGR(44, 39, 46),
    RGB_to_BGR(117, 49, 136),
    RGB_to_BGR(230, 9, 101),
    RGB_to_BGR(249, 72, 146),
    RGB_to_BGR(255, 161, 201),
    RGB_to_BGR(251, 229, 229),
    RGB_to_BGR(15, 14, 14),
    RGB_to_BGR(84, 18, 18),
    RGB_to_BGR(139, 154, 70),
    RGB_to_BGR(238, 238, 238),
    RGB_to_BGR(7, 34, 39),
    RGB_to_BGR(53, 133, 139),
    RGB_to_BGR(79, 189, 186),
    RGB_to_BGR(174, 254, 255)]

def color_lerp(c, d, percent):
    blue = lerp(c[0], d[0], percent) 
    green = lerp(c[1], d[1], percent) 
    red = lerp(c[2], d[2], percent)
    return (blue, green, red)

def lerp (color_a, color_b, percent):
    a = color_a * (1-percent)
    b = color_b * percent
    return a + b;

def gen_jpg (t_l_Color, t_r_Color, b_l_Color, b_r_Color, name):
    output = np.zeros((h,w,3),np.uint8)
    for j in range (w):
        percent_w = j / w
        for i in range(h):
            percent_h = i / h
            if j == 0 & i == 0:
                output[i,j] = t_l_Color
            if j == w-1 & i == 0:
                output[i,j]= t_r_Color
            if j == 0 & i == h-1:
                output[i,j] = b_l_Color
            if j == w-1 & i == h-1:
                output[i,j] = b_r_Color
            else:
                a = color_lerp(t_l_Color, t_r_Color, percent_w)
                b = color_lerp(b_l_Color, b_r_Color, percent_w)
                output[i,j] = color_lerp(a, b, percent_h)
    cv2.imwrite(name,output)   

top_l_color = (0,0,0)
top_r_color = (0,0,0)
botom_l_color = (0,0,0)
botom_r_color = (0,0,0)

top_l_final = (0,0,0)
top_r_final = (0,0,0)
botom_l_final = (0,0,0)
botom_r_final = (0,0,0)

route = 'gfx/'
name = 'test_'
ext = '.jpg'

def gen_animation(fps, duration, k):
    frames = fps * duration
    for i in range(frames):
        percent = i / frames
        a = color_lerp(top_l_color, top_l_final, percent)
        b = color_lerp(top_r_color, top_r_final, percent)
        c = color_lerp(botom_l_color, botom_l_final, percent)
        d = color_lerp(botom_r_color, botom_r_final, percent)
        numb = i + (k * frames)
        aux = route + name + str(numb) + ext;
        print(aux)
        gen_jpg(a,b,c,d,aux)

final = []

for i in range(4):
    idx = rnd.randint(0,len(palette)-1)
    final.append(palette[idx])

for jdx in range(8):
    top_l_color = final[0]
    top_r_color = final[1]
    botom_r_color = final[2]
    botom_l_color  = final[3]
    final = []

    for j in range(4):
        idx = rnd.randint(0,len(palette)-1)
        final.append(palette[idx])

    top_l_final  = final[0]
    top_r_final = final[1]
    botom_r_final = final[2]
    botom_l_final = final[3]

    gen_animation(50,2, jdx)

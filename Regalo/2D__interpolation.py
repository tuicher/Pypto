import cv2
import numpy as np

# twt resolution = 640x640
w = 640
h = 640

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

# inicial
top_l_color = RGB_to_BGR(229, 153, 52)
top_r_color = RGB_to_BGR(154, 230, 110)
botom_l_color  = RGB_to_BGR(44, 39, 46)
botom_r_color = RGB_to_BGR(117, 49, 136)

# final
top_l_final  = botom_l_color
top_r_final = top_l_color
botom_r_final = top_r_color
botom_l_final = botom_r_color


#top_l_final = RGB_to_BGR(93, 107, 108)
#top_r_final =  RGB_to_BGR(66, 70, 66)
#botom_l_final = RGB_to_BGR(192, 96, 20)
#botom_r_final = RGB_to_BGR(190, 105, 20)

route = 'gfx/'
name = 'test_'
ext = '.jpg'

def gen_animation(fps, duration):
    frames = fps * duration
    for i in range(frames):
        percent = i / frames
        a = color_lerp(top_l_color, top_l_final, percent)
        b = color_lerp(top_r_color, top_r_final, percent)
        c = color_lerp(botom_l_color, botom_l_final, percent)
        d = color_lerp(botom_r_color, botom_r_final, percent)
        aux = route + name + str(i) + ext;
        print(aux)
        gen_jpg(a,b,c,d,aux)

gen_animation(60,10)


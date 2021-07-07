import cv2
from math import cos, sin, pi
from math import floor, ceil
import numpy as np


img_path = "./img/python_logo.png"
np_img = cv2.imread(img_path)
list_img = np_img.tolist()

print(len(list_img))
print(len(list_img[0]))
print(len(list_img[0][0]))


def getMat(scale, angle, translation=None):
    if translation is None:
        translation = [0, 0]
    
    scale = 1./scale   
    c = scale*cos(-angle*pi/180)
    s = scale*sin(-angle*pi/180)
    return [[c, -s, translation[0]], [s, c, translation[1]]]


def affine(centre, point, scale, M):
    nx = centre[0] + (point[0]-centre[0]*scale) * M[0][0] + (point[1]-centre[1]*scale) * M[0][1] + M[0][2]/scale
    ny = centre[1] + (point[0]-centre[0]*scale) * M[1][0] + (point[1]-centre[1]*scale) * M[1][1] + M[1][2]/scale
    return nx, ny


H, W, C = len(list_img), len(list_img[0]), len(list_img[0][0])

scale = 1.7
angle = 137
translation = [30, -30]
M = getMat(scale, angle, translation)

centre = [H//2, W//2]
scaled_H, scaled_W = int(H*scale), int(W*scale)
tmp_img = [[[0]*C for _ in range(scaled_W)] for _ in range(scaled_H)]

for x in range(scaled_H):
    for y in range(scaled_W):
        nx, ny = affine(centre, (x, y), scale, M)
        if 0 <= nx <= H-1 and 0 <= ny <= W-1:
            nx_f = floor(nx)
            nx_c = ceil(nx)
            ny_f = floor(ny)
            ny_c = ceil(ny)
            
            h = nx - nx_f
            w = ny - ny_f
            
            for c in range(len(list_img[0][0])):
                try:
                    pix1 = list_img[nx_f][ny_f][c]
                    pix2 = list_img[nx_c][ny_f][c]
                    pix3 = list_img[nx_f][ny_c][c]
                    pix4 = list_img[nx_c][ny_c][c]
                    
                    pix_value = int((1-h)*(1-w)*pix1 + h*(1-w)*pix2 + \
                        (1-h)*w*pix3 + h*w*pix4)
                    tmp_img[x][y][c] = pix_value
                except:
                    pass


rot_img = np.array(tmp_img).astype(np.uint8)
cv2.imshow("Rotated Img", rot_img)
cv2.imshow("Original Img", np_img)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
from math import cos, sin, pi
from math import floor, ceil
import numpy as np


def getRotateM(angle):
    c = cos(-angle*pi/180)
    s = sin(-angle*pi/180)
    return [[c, -s], [s, c]]


def rotatePos(cx, cy, px, py, M):
    nx = cx + (px-cx) * M[0][0] + (py-cy) * M[0][1]
    ny = cy + (px-cx) * M[1][0] + (py-cy) * M[1][1]
    return nx, ny


def rotate(img, angle=90):
    if isinstance(img, np.ndarray):
        img = img.tolist()
    elif isinstance(img, list):
        img = img
    else:
        raise TypeError("Only support ndarray or list type img")

    M = getRotateM(angle)
    H, W, C = len(img), len(img[0]), len(img[0][0])
    cx, cy = H//2, W//2

    tmp_img = [[[0]*C for _ in range(W)] for _ in range(H)]
    for x in range(len(img)):
        for y in range(len(img[0])):
            nx, ny = rotatePos(cx, cy, x, y, M)

            if 0 <= nx <= H-1 and 0 <= ny <= W-1:
                nx_f = floor(nx)
                nx_c = ceil(nx)
                ny_f = floor(ny)
                ny_c = ceil(ny)
                
                h = nx - nx_f
                w = ny - ny_f
                
                for c in range(len(img[0][0])):
                    try:
                        pix1 = img[nx_f][ny_f][c]
                        pix2 = img[nx_c][ny_f][c]
                        pix3 = img[nx_f][ny_c][c]
                        pix4 = img[nx_c][ny_c][c]
                        
                        pix_value = int((1-h)*(1-w)*pix1 + h*(1-w)*pix2 + \
                            (1-h)*w*pix3 + h*w*pix4)
                        tmp_img[x][y][c] = pix_value
                    except:
                        pass
    return tmp_img


if __name__ == "__main__":
    img_path = "./img/python_logo.png"
    np_img = cv2.imread(img_path)
    list_img = np_img.tolist()

    rot_img = rotate(list_img, angle=137)
    rot_img = np.array(rot_img).astype(np.uint8)
    cv2.imshow("Rotated Img", rot_img)
    cv2.imshow("Original Img", np_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
import cv2
from math import cos, sin, pi
from math import floor, ceil
import numpy as np


img_path = "./python_logo.png"
np_img = cv2.imread(img_path)
list_img = np_img.tolist()

print(len(list_img))
print(len(list_img[0]))
print(len(list_img[0][0]))



scale = 1.7
H, W, C = len(list_img), len(list_img[0]), len(list_img[0][0])
scaled_H, scaled_W = int(H*scale), int(W*scale)


tmp_img = [[[0]*C for _ in range(scaled_W)] for _ in range(scaled_H)]
for x in range(scaled_H):
    for y in range(scaled_W):
        nx, ny = x/scale, y/scale
        
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
cv2.imshow("Scaled Img", rot_img)
cv2.imshow("Original Img", np_img)
cv2.waitKey()
cv2.destroyAllWindows()
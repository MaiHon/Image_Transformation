import cv2
from math import cos, sin, pi
import numpy as np


img_path = "./python_logo.png"
np_img = cv2.imread(img_path)
list_img = np_img.tolist()

print(len(list_img))
print(len(list_img[0]))
print(len(list_img[0][0]))


def getTranslatedPos(x, y, dx, dy):
    return min(H-1, max(0, x+dx)), min(W-1, max(0, y+dy))


dx, dy = 130, -30
H, W, C = len(list_img), len(list_img[0]), len(list_img[0][0])
tmp_img = [[[0]*C for _ in range(W)] for _ in range(H)]
for x in range(H):
    for y in range(W):
        nx, ny = getTranslatedPos(x, y, dx, dy)
        
        for c in range(C):
            tmp_img[nx][ny][c] = list_img[x][y][c]


rot_img = np.array(tmp_img).astype(np.uint8)
cv2.imshow("Translated Img", rot_img)
cv2.imshow("Original Img", np_img)
cv2.waitKey()
cv2.destroyAllWindows()